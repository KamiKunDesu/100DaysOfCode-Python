'''This class is going to be responsible for making coffee - it simply makes the different coffees 
and does nothing else'''
from coin_handler import CoinHandler
from resource_manager import ResourceManager
import sys
import time
import re

class CoffeeMaker:
    '''This is the coffee maker which will handle making actual coffees'''

    def __init__(self):
        '''The init function makes sure to keep track of the cost of each function as well as give a
        resource manager and coin handler to the class'''
        
        # Stored in the form of lists from left to right cost in cents, water, milk, coffee
        self.coffee_resource_cost = {
            'latte': [2.50, 200, 150, 24],
            'espresso': [1.50, 50, 0, 18],
            'cappuccino': [3.00, 250, 100, 24],
        }

        self.coin_handler = CoinHandler()

        self.resource_manager = ResourceManager()

    def make_coffee(self, coffee_type):
        '''This function makes a coffee with the help of the resource manager and the
        coin handler'''

        # get the resource amounts required to make the coffee
        cost = self.coffee_resource_cost[coffee_type][0]
        water = self.coffee_resource_cost[coffee_type][1]
        milk = self.coffee_resource_cost[coffee_type][2]
        coffee = self.coffee_resource_cost[coffee_type][3]

        # Tell them how much it will cost
        print(f"That will cost ${cost:.2f}")
        time.sleep(1)

        # Ask the coin handler to process the coins in
        amount_in, coins_given = self.coin_handler.process_coins_in()

        # Ask the resource manager if it has enough resources
        resources_available = self.resource_manager.check_available_resources(water, milk, coffee)

        # Ask the coin handler if it has enough change to give back
        optimal_change = self.coin_handler.sufficient_change_available(amount_in, cost)

        # If the coin handler doesn't have sufficient change
        if not optimal_change:
            print("Sorry, the machine does not have sufficient change to fulfill your request")
            time.sleep(1)
            # Then return the coins that were given
            self.coin_handler.return_coins(coins_given, False)

        # If the resources are insufficient
        elif not resources_available:
            print("Sorry, the machine doesn't have enough resources to fulfill your request")
            time.sleep(1)
            # Then return the coins that were given
            self.coin_handler.return_coins(coins_given, False)

        # Handle successful transaction with no change needed
        elif optimal_change == 'none':
            print(f"No problem making you {coffee_type} now.")
            time.sleep(1)
            # Remove the resources from the system
            self.resource_manager.give_resources_for_coffee(water, milk, coffee)

            # Print a wait message for UI experience
            print("Making...")
            time.sleep(1)
            for i in range (3):
                print(3 - i)
                time.sleep(1)
            print("Complete! Now let me get your change")
            time.sleep(1)

            # Return the change
            print("No change required, have a nice day!")

        # Otherwise the request can be successfully handled
        else:
            print(f"No problem making you {coffee_type} now.")
            time.sleep(1)
            # Remove the resources from the system
            self.resource_manager.give_resources_for_coffee(water, milk, coffee)

            # Print a wait message for UI experience
            print("Making...")
            time.sleep(1)
            for i in range (3):
                print(3 - i)
                time.sleep(1)
            print("Complete! Now let me get your change")
            time.sleep(1)

            # Return the change
            self.coin_handler.return_coins(optimal_change, True)

