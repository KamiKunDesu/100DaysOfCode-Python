'''This is the main coffee machine program which will be what runs'''
from coffee_machine import CoffeeMachine

def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.machine_on()

if __name__ == '__main__':
    main()