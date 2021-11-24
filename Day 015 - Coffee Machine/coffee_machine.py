'''This is the coffee machine class for the main program'''
import sys
import time
import re
from coffee_maker import CoffeeMaker
class CoffeeMachine:
    '''This is the coffee machine class'''
    
    def __init__(self):
        '''This is the init variables that sets the initial state of the machine'''
        
        # Gives the class a coffee maker which implicitly gives it a coin handler and resource manager
        self.coffee_maker = CoffeeMaker()

    def machine_on(self):
        '''This is going to be the main machine routine which loops through until system off is called'''
        while True:
            # First get the input
            user_input = self.get_input()

            # Handle consequences
            if user_input == "latte":
                self.coffee_maker.make_coffee(user_input)
            elif user_input == "espresso":
                self.coffee_maker.make_coffee(user_input)
            elif user_input == "cappuccino":
                self.coffee_maker.make_coffee(user_input)
            elif user_input == "replenish":
                self.coffee_maker.resource_manager.replenish()
            elif user_input == "report":
                self.print_report()
            elif user_input == "off":
                self.machine_off()
            else:
                continue

    def get_input(self):
        '''This is going to be a helper function that gets the user input on from the machine'''
        
        # Make a while loop with an input flag and counter to give a valid input
        counter = 10
        input_flag = False
        while counter and not input_flag:
            # Get user input
            user_input = input("Would you like a latte, an espresso or a cappuccino? ")
            time.sleep(1)

            # Use various regex patterns to match one of the following patterns
            if re.compile("[Ll][Aa][Tt][Tt][Ee]").fullmatch(user_input):
                user_input = "latte"
                input_flag = True
            elif re.compile("[Ee][Ss][Pp][Rr][Ee][Ss][Ss][Oo]").fullmatch(user_input):
                user_input = "espresso"
                input_flag = True
            elif re.compile("[Cc][Aa][Pp][Pp][Uu][Cc][Cc][Ii][Nn][Oo]").fullmatch(user_input):
                user_input = "cappuccino"
                input_flag = True
            elif re.compile("[Rr][Ee][Pp][Oo][Rr][Tt]").fullmatch(user_input):
                user_input = "report"
                input_flag = True
            elif re.compile("[Rr][Ee][Pp][Ll][Ee][Nn][Ii][Ss][Hh]").fullmatch(user_input):
                user_input = "replenish"
                input_flag = True
            elif re.compile("[Oo][Ff][Ff]").fullmatch(user_input):
                user_input = "off"
                input_flag = True
            else:
                counter -= 1
                if not counter:
                    print("Too many invalid inputs given - the system will now exit.")
                    time.sleep(4)
                    sys.exit()
                print("Please give a valid input: 'Latte', 'Espresso' or 'Cappuccino'")
        
        # Return the user input
        return user_input

    def print_report(self):
        '''This function prints a report of all the current resources necessary'''
        
        print(f"This machine has {self.coffee_maker.resource_manager.resources['water']}ml of water")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.resource_manager.resources['milk']}ml of milk")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.resource_manager.resources['coffee']}g of coffee")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.coin_handler.change_held['quarters']} quarters")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.coin_handler.change_held['dimes']} dimes")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.coin_handler.change_held['nickels']} nickels")
        time.sleep(1)
        print(f"This machine has {self.coffee_maker.coin_handler.change_held['cents']} cents")
        time.sleep(1)

    def machine_off(self):
        '''This turns the machine off'''
        
        print("The machine will now turn off")
        time.sleep(4)
        sys.exit()