'''This class is going to be responsible for monitoring the resources in the system - it will have functions for refilling
the machine as well as for checking that there are acceptable resources for making a coffee'''
import time
import sys
import re

class ResourceManager:
    '''This is the resource manager class responsible for handling the resources in the system'''

    def __init__(self):
        '''The init function for the initial state of the system which gives an initial amount of resources'''
        
        # Add resources
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def check_available_resources(self, water: int, milk: int, coffee: int) -> bool:
        '''This function checks that there are resources available in the coffee machine to make the coffee'''
        
        # Make returns
        if water > self.resources['water']:
            return False
        elif milk > self.resources['milk']:
            return False
        elif coffee > self.resources['coffee']:
            return False
        # All resources sufficient so give back true
        else:
            return True
        
    def give_resources_for_coffee(self, water: int, milk: int, coffee: int):
        '''This function reduces the resources in the machine'''

        # Remove resources from the system as they're given out
        self.resources['water'] -= water
        self.resources['milk'] -= milk
        self.resources['coffee'] -= coffee

        return
    
    def replenish(self):
        '''This is the main replenish method which uses one of the helper methods to replenish resources
        in the coffee machine'''

        # Going to use two while loop blocks, on with a try except block to get a valid input with 
        # Some regex to make sure the input is correct
        counter = 10
        input_flag = False
        while counter and not input_flag:
            resource = input("What would you like to replenish?: ")
            time.sleep(1)
            if re.compile('[Cc][Oo][Ff][Ff][Ee][Ee]').fullmatch(resource):
                resource = "coffee"
                input_flag = True
            elif re.compile('[Mm][Ii][Ll][Kk]').fullmatch(resource):
                resource = 'milk'
                input_flag = True
            elif re.compile('[Ww][Aa][Tt][Ee][Rr]').fullmatch(resource):
                resource = 'water'
                input_flag
            else:
                counter -= 1
                if not counter:
                    print("Too many invalid inputs, the system will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Invalid input, please type one of Water, Milk or Coffee")
                time.sleep(1)
        
        # Next we need to get the amount
        counter = 10
        input_flag = False
        while counter and not input_flag:
            try:
                amount = int(input("How much are you putting in?: "))
                time.sleep(1) 
            except ValueError:
                counter -= 1
                if not counter:
                    print("Too many invalid inputs, the system will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please give a valid integer input")
                time.sleep(1)
                continue
            if amount <= 0:
                counter -= 1
                if not counter:
                    print("Too many invalid inputs, the system will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please give an amount above 0")
                time.sleep(1)
            else:
                input_flag = True
        
        # Finally, call the method that needs to be called depending on which resource
        if resource == "coffee":
            self.replenish_coffee(amount)
        elif resource == "water": 
            self.replenish_water(amount)
        elif resource == "milk":
            self.replenish_milk(amount)
        
        return

    def replenish_milk(self, amount):
        '''Helper method to replenish the milk'''
        self.resources['milk'] += amount
        print(f'Milk replenished with {amount}ml')
        time.sleep(1)
        return

    def replenish_coffee(self, amount):
        '''Helper method to replenish the coffee'''
        self.resources['coffee'] += amount
        print(f'Coffee replenished with {amount}g')
        time.sleep(1)
        return

    def replenish_water(self, amount):
        '''Helper method to replenish the water'''
        self.resources['water'] += amount
        print(f'Water replenished with {amount}ml')
        time.sleep(1)
        return