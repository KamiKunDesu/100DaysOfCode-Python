'''This file is going to be a class that handles all of the coins of the machine - handles processing coins in
as well as giving change back out and keeps an eye on the level of each coin'''
import time
import sys

class CoinHandler:
    '''This class handles all coins in the machine'''

    def __init__(self):
        '''The initial state of the class'''
        self.change_held = {
            'quarters': 5,
            'dimes': 10,
            'nickels':15,
            'cents': 50,
        }

    def process_coins_in(self):
        '''This function is going to process the coins the user puts in by counting the number of quarters
        dimes, nickels and cents they give to the system as well as temporarily adding them to the system'''

        # Get the amount of each coin
        quarter_amount = self.get_coin_input("quarters")
        dime_amount = self.get_coin_input("dimes")
        nickel_amount = self.get_coin_input("nickels")
        cent_amount = self.get_coin_input("cents")

        # Add the coins into stock
        self.change_held['quarters'] += quarter_amount
        self.change_held['dimes'] += dime_amount
        self.change_held['nickels'] += nickel_amount
        self.change_held['cents'] += cent_amount

        # Sum the total amount of all the inputted coins
        total_amount = quarter_amount*0.25 + dime_amount*0.1 + nickel_amount*0.05 + cent_amount*0.01
        
        # Make the coin list of coins given
        coins_given = []
        for i in range(quarter_amount):
            coins_given.append(0.25)
        for i in range(dime_amount):
            coins_given.append(0.10)
        for i in range(nickel_amount):
            coins_given.append(0.05)
        for i in range(cent_amount):
            coins_given.append(0.01) 

        return total_amount, coins_given

    def get_coin_input(self, coin_type: str) -> int:
        '''Because we have to get the coins like 4 times it's easier to just have this helper 
        method to call for each coin denomination'''
        # These are two flags to help prevent an infinite loop on the program
        counter = 10
        input_flag = False
        while counter and not input_flag:
            try:
                # Try to get amount 
                coin_amount = int(input(f"How many {coin_type} will you put in?: "))
                time.sleep(1)
                # Make sure that if it's a valid integer it's also positive
                if coin_amount < 0:
                    counter -= 1
                    # Handle too many bad inputs
                    if not counter:
                        print("Too many invalid inputs, the system will now exit")
                        time.sleep(4)
                        sys.exit()
                    print("Please enter a valid positive integer amount")
                    continue
                else:
                    # Break loop if valid input
                    input_flag = True
            except ValueError:
                # Handle too many bad non integer inputs
                counter -= 1
                if not counter:
                    print("Too many invalid inputs, the system will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please enter a valid positive integer amount")
        
        return coin_amount

    def calculate_change_needed(self, total_cost, amount_given):
        '''This function calculates the amount of change needed to be given back'''
        return round(amount_given - total_cost, 2)

    def get_coins_from_dict(self):
        '''This method is a helper method for checking if the machine has the required amount of
        change to give back to the customer, first we need to make a list of all the coins currently
        in the system'''

        # We start with an empty list
        coin_list = []

        # Then we loop through each coin and how much of that coin there is and append the value to the list
        # For as many times as the coin exists in the system
        for i in range(self.change_held['cents']):
            coin_list.append(0.01)
        for i in range(self.change_held['nickels']):
            coin_list.append(0.05)
        for i in range(self.change_held['dimes']):
            coin_list.append(0.10)
        for i in range(self.change_held['quarters']):
            coin_list.append(0.25)

        return coin_list

    def flatten(self, coin_list):
        '''This method flattens lists, it is used as a helper method to flatten the list produced by
        the change_available method'''
        for item in coin_list:
            try:
                yield from self.flatten(item)
            except:
                yield item

    def optimal_change_calc(self, to_return, coin_list):
        '''This method recursively calculates the amount of coins that are necessary to fulfill a change
        request so that we can see the optimal return strategy and if we have enough coins available'''
        
        # This flag indicates if there is no denomination less than the amount to return then we've bottomed out our function
        flag = None
        # iterate through every coin in the list
        for c in coin_list:
            # If the amount to return is the same as the amount in the list then we simply give back that coin
            if c == to_return: return [c]
            # Otherwise keep going up the chain and as long as the coin value is less than the total amount we should set that as the new flag
            if c < to_return:
                flag = c
        # At the end of this, as long as a coin was chosen we should remove it from the list (because we'll already have used it)
        if flag != None:
            coin_list.remove(flag)
        else:
            # if we didn't find a coin that works return a 0 (this also signifies we have insufficient change)
            return [0]
        # The remaining amount to return is the previous amount take away the new coin
        temp_balance = round(to_return - flag, 2)
        # Return the list with the flag in it + the list of the result of recursively calling - this will of course
        # Lead to the function ultimately returning a nested list which will need to be flattened
        return [flag] + [self.optimal_change_calc(temp_balance, coin_list)]

    def sufficient_change_available(self, amount_given, cost):
        '''This method checks if there is the correct change'''

        # First we need to get a list of all the coins in the machine so that the function can work with it
        coin_list = self.get_coins_from_dict()
        # Then we get how much change is required
        change_required = self.calculate_change_needed(cost, amount_given)
        # First let's handle if no change required
        if not change_required:
            return "none"
        # Then we use the change available function to check that we have enough change to give back
        optimal_change = self.optimal_change_calc(change_required, coin_list)
        # Since we get a nested list back we will need to flatten it
        optimal_change = list(self.flatten(optimal_change))
        if 0 in optimal_change:
            return None
        else:
            return optimal_change

    def return_coins(self, coin_list, print_message: bool):
        '''This function returns coins and removes them from stock'''

        # Make a change required for the message variable
        change_required = sum(coin_list)

        # Loop through and remove the coins from stock
        for i in range(coin_list.count(0.25)):
            self.change_held['quarters'] -= 1
        for i in range(coin_list.count(0.10)):
            self.change_held['dimes'] -= 1
        for i in range(coin_list.count(0.05)):
            self.change_held['nickels'] -= 1
        for i in range(coin_list.count(0.01)):
            self.change_held['cents'] -= 1

        # Print the appropriate message
        if print_message:
            self.print_message_one(coin_list, change_required)
        else:
            self.print_message_two(coin_list, change_required)

    def print_message_one(self, coin_list, change_required):
        '''This prints the message of a successful transaction'''

        # This is a clever concatenated f string with conditionals to give an appropriate response for the amount of change given, if no denominations of a certain coin are given
        # Then a boolean condition (which evaluates in integer form as 1 for true and 0 for false) paired with pythons string multiplication
        # Excludes strings about coins where 0 are returned and includes strings where they are returned
        # It uses this same logic to decide wether to pluralize the coin denomination amount in the string
        print(f"Your change comes to {change_required:.2f}\n" + f"Machine now dispensing: \n" + f"{coin_list.count(0.25)} quarter{'s'*(coin_list.count(0.25) > 1)}\n"*(0.25 in coin_list) + f"{coin_list.count(0.10)} dime{'s'*(coin_list.count(0.10) > 1)}\n"*(0.1 in coin_list) + 
        f"{coin_list.count(0.05)} nickel{'s'*(coin_list.count(0.05) > 1)}\n"*(0.05 in coin_list) + f"{coin_list.count(0.01)} cent{'s'*(coin_list.count(0.01) > 1)}\n"*(0.01 in coin_list) + f"for a total of {change_required:.2f}\n")
        time.sleep(1)

    def print_message_two(self, coin_list, change_required):
        '''This print the message for returning coins from an unsuccessful transaction'''

        # This is a clever concatenated f string with conditionals to give an appropriate response for the amount of change given, if no denominations of a certain coin are given
        # Then a boolean condition (which evaluates in integer form as 1 for true and 0 for false) paired with pythons string multiplication
        # Excludes strings about coins where 0 are returned and includes strings where they are returned
        # It uses this same logic to decide wether to pluralize the coin denomination amount in the string
        print(f"You gave in total {change_required:.2f} which needs to be returned\n" + f"Machine now dispensing: \n" + f"{coin_list.count(0.25)} quarter{'s'*(coin_list.count(0.25) > 1)}\n"*(0.25 in coin_list) + f"{coin_list.count(0.10)} dime{'s'*(coin_list.count(0.10) > 1)}\n"*(0.1 in coin_list) + 
        f"{coin_list.count(0.05)} nickel{'s'*(coin_list.count(0.05) > 1)}\n"*(0.05 in coin_list) + f"{coin_list.count(0.01)} cent{'s'*(coin_list.count(0.01) > 1)}\n"*(0.01 in coin_list) + f"for a total of {change_required:.2f}\n")
        time.sleep(1)

    