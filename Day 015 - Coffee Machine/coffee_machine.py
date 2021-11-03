'''This is the coffee machine class for the main program'''

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

    def machine_on(self):
        pass

    def machine_off(self):
        pass

    def print_report(self):
        pass

    def resource_check(self):
        pass

    def process_coins_in(self):
        pass

    def process_coins_out(self):
        pass

    def make_espresso(self):
        pass

    def make_latte(self):
        pass

    def make_cappuccino(self):
        pass

    def get_coins_from_dict(self):
        '''This funcition is a helper function for checking if the machine has the required amount of
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
        '''This function recursively calculates the amount of coins that are necessary to fulfill a change
        request so that we can see the optimal return strategy and if we have enough coins available'''
        
        flag = None
        for c in coin_list:
            if c == to_return: return c
            if c < to_return:
                flag = c
        if flag != None:
            coin_list.pop(flag)
        temp_balance = round(to_return - flag, 2)
        return [flag] + [self.change_available(temp_balance, coin_list)]

    def flatten(self, coin_list):
        '''This function flattens lists, it is used as a helper function to flatten the list produced by
        the change_available function'''
        for item in coin_list:
            try:
                yield from flatten(item)
            except:
                yield item

    def return_change(self, amount_given, cost):
        '''This function calculates if there is correct change to give change and then returns it if there is'''
        coin_list = self.get_coins_from_dict()
        change_required = amount_given - cost
        optimal_change = self.change_available(change_required, coin_list)
        optimal_change = list(self.flatten(optimal_change))
        if None in optimal_change:
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
            return optimal_change

    def replenish_milk(self):
        pass

    def replenish_coffee(self):
        pass

    def replenish_water(self):
        pass

            




