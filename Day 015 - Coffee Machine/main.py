'''
Day 15 of 100 days of code python challenge - The purpose of this project is to make a coffee machine
schema which has the ability to make different coffee's all whilst managing the resources that are being
taken out of and put into the machine
'''
from coffee_machine import CoffeeMachine

def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.machine_on()

if __name__ == '__main__':
    main()