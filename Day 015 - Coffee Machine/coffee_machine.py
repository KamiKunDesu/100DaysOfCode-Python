'''This is the coffee machine class for the main program'''
import sys
import time
import re
class CoffeeMachine:
    '''This is the coffee machine class'''
    
    def __init__(self):
        '''This is the init variables that sets the initial state of the machine'''
        
        self.change_held = {
            'quarters': 5,
            'dimes': 10,
            'nickels':15,
            'cents': 50,
        }

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        # Stored in the form of lists  cost in cents, 
        self.coffee_resource_cost = {

        }

    def machine_on(self):
        pass

    def machine_off(self):
        '''This method turns the machine off'''
        print("The system is now turning off")
        time.sleep(4)
        sys.exit()

    def print_report(self):
        '''This method prints a report of how much resources the system has'''
        # Get all the relevant variables
        quarters_amount = self.change_held['quarters']
        dimes_amount = self.change_held['dimes']
        nickels_amount = self.change_held['nickels']
        cents_amount = self.change_held['cents']
        water_amount = self.resources['water']
        milk_amount = self.resources['milk']
        coffee_amount = self.resources['coffee'] 
        # Print out the report 
        print(
            f"The machine has the following: "
            f"{quarters_amount} quarters"
            f"{dimes_amount} dimes"
            f"{nickels_amount} nickels"
            f"{dimes_amount} dimes"
            f"{cents_amount} cents"
            f"{water_amount}ml of water"
            f"{milk_amount}ml of milk"
            f"{coffee_amount}g of coffee"
        )
            
    def resource_check(self, water, coffee, milk):
        '''This is a helper method for the different drink maker functions which checks that the
        machine has enough resources available to make the drink'''
        
        # A simple if else check with a bool response to return if the amount of resources is correct
        if self.resources['water'] >= water and self.resources['coffee'] >= coffee and self.resources['milk'] >= milk:
            return True
        else:
            return False

    def process_coins_in(self, cost):
        '''This function is going to process the coins the user puts in by counting the number of quarters
        dimes, nickels and cents they give to the system as well as temporarily adding them to the system'''
        
        # Get the amount of each coin
        quarter_amount = self.get_coin_input("quarters")
        dime_amount = self.get_coin_input("dimes")
        nickel_amount = self.get_coin_input("nickels")
        cent_amount = self.get_coin_input("cents")

        # Sum the total amount of all the inputted coins
        total_amount = quarter_amount*0.25 + dime_amount*0.1 + nickel_amount*0.05 + cent_amount*0.01
    
    def get_coin_input(self, coin_type: str) -> int:
        '''Because we have to get the coins like 4 times it's easier to just have this helper method to call for each coin denomination'''
        counter = 10
        input_flag = False
        while counter and not input_flag:
            try:
                # Try to get amount 
                coin_amount = int(input(f"How many {coin_type} will you put in "))
                time.sleep(1)
                # Make sure that if it's a valid integer it's also positive
                if coin_amount < 0:
                    counter -= 1
                    # Handle too many bad inputs
                    if not counter:
                        print("To many invalid inputs, the system will now exit")
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
                    print("To many invalid inputs, the system will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please enter a valid positive integer amount")
        
        return coin_amount

    def refund_coins_for_insufficient_amount(total_amount, cost):
        if 

    def make_espresso(self):
        pass

    def make_latte(self):
        pass

    def make_cappuccino(self):
        pass

    def get_coins_from_dict(self):
        '''This method is a helper method for checking if the machine has the required amount of
        change to give back to the customer, first we need to make a list of all the coins currently
        in the system'''

        coin_list = []

        for i in range(self.coins_dict['cents']):
            coin_list.append(0.01)
        for i in range(self.coins_dict['nickels']):
            coin_list.append(0.05)
        for i in range(self.coins_dict['dimes']):
            coin_list.append(0.10)
        for i in range(self.coins_dict['quarters']):
            coin_list.append(0.25)

        return coin_list
    
    def change_available(self, to_return, coin_list):
        '''This method recursively calculates the amount of coins that are necessary to fulfill a change
        request so that we can see the optimal return strategy and if we have enough coins available'''
        
        flag = None
        for c in coin_list:
            if c == to_return: return c
            if c < to_return:
                flag = c
        if flag != None:
            coin_list.pop(flag)
        else:
            return 0
        temp_balance = round(to_return - flag, 2)
        return [flag] + [self.change_available(temp_balance, coin_list)]

    def flatten(self, coin_list):
        '''This method flattens lists, it is used as a helper method to flatten the list produced by
        the change_available method'''
        for item in coin_list:
            try:
                yield from flatten(item)
            except:
                yield item

    def return_change(self, amount_given, cost):
        '''This method calculates if there is correct change to give change and then returns it if there is'''
        coin_list = self.get_coins_from_dict()
        change_required = amount_given - cost
        optimal_change = self.change_available(change_required, coin_list)
        optimal_change = list(self.flatten(optimal_change))
        if 0 in optimal_change:
            print("Sorry, insufficient coins to produce change")
            return None
        else:
            for i in range(optimal_change.count(0.25)):
                self.change_held['quarters'] -= 1
            for i in range(optimal_change.count(0.10)):
                self.change_held['dimes'] -= 1
            for i in range(optimal_change.count(0.05)):
                self.change_held['nickels'] -= 1
            for i in range(optimal_change.count(0.01)):
                self.change_held['cents'] -= 1
            # This is a clever concatenated f string with conditionals to give an appropriate response for the amount of change given
            print(f"Your change comes to {change_required}\n" + f"Machine now dispensing: \n" + f"{optimal_change.count(0.25)} quarters\n"*(0.25 in optimal_change) + f"{optimal_change.count(0.10)} dimes\n"*(0.1 in optimal_change) + 
            f"{optimal_change.count(0.05)} nickels\n"*(0.05 in optimal_change) + f"{optimal_change.count(0.01)} cents\n"*(0.01 in optimal_change) + f"for a total of {change_required}\n")
            time.sleep(1)
            return optimal_change

    def replenish_milk(self):
        pass

    def replenish_coffee(self):
        pass

    def replenish_water(self):
        pass