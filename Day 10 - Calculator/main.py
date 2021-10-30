'''
Day 10 of 100 days of code python challenge - The purpose of this project is to make a calculator program
which essentially takes numbers and operators and calculates the result for the user.
'''
from Calculator_Class import Calculator
import sys
import time
import re

# Function to check if more operations are needed
def another_operation() -> bool:
    counter = 10
    while counter > 0:
        more_operations = input("Do you want to do any more operations on the result?: ")
        # Check if input something like Yes, returns false to keep the while block in main func going
        if re.compile('[Yy](es|ES)?').fullmatch(more_operations):
            return True
         # Check if input something like No, returns true to break the while block in the main func
        elif re.compile('[Nn](o|O)?').fullmatch(more_operations):
            return False
        # If not valid input reduce counter and restart while loop, if counter is 0 exit
        else:
            counter -= 1
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(3)
                sys.exit()
            print("Please give a valid input - 'Yes' or 'No'")



# Make a main function to hold the program

def main():
    '''The main function'''

    # Initialize our calculator object
    calculator = Calculator()

    #print the intro
    print('''
                   _            _       _                 
          ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
         / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__/
        | (_| (_| | | (__| |_| | | (_| | || (_) | |  
         \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
         |  _________________  |
         | | JO           0. | |
         | |_________________| |
         |  ___ ___ ___   ___  |
         | | 7 | 8 | 9 | | + | |
         | |___|___|___| |___| |
         | | 4 | 5 | 6 | | - | |
         | |___|___|___| |___| |
         | | 1 | 2 | 3 | | x | |
         | |___|___|___| |___| |
         | | . | 0 | = | | / | |
         | |___|___|___| |___| |
         |_____________________|
    ''')

    # Go through the motions of computing the first input
    computed_num = calculator.calculate_first_input()

    # Get the continue flag to see if more input needed
    continue_flag = another_operation()

    # A while loop that keeps on asking for subsequent inputs if needed
    while continue_flag:
        computed_num = calculator.calculate_subsequent_input(computed_num)
        continue_flag = another_operation()
    
    print("Thanks for using the calculator, the system will now exit")
    time.sleep(5)
    sys.exit()


main()
