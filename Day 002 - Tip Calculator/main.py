'''
The purpose of this "Day 2" project is to make a program which can calculate the tip you should pay
at a restaurant. A quick and easy calculator for this purpose. The general purpose of the project is
to learn about mathematical operations in python as well as type conversion.
'''
import sys

#Greeting
print('Welcome to the tip calculator. Let\'s get the tip calculated!')

#initialise counter variable
i = 0

#Bring on a bill price variable, inside a while block with a try block inside to ensure correct input
while i < 10:
    bill_price = input("How much was the bill? £")
    try:
        bill_price = float(bill_price)
        if bill_price >= 0:
            break
        else:
            print('The price of the meal can\'t be less than 0!!')
    except ValueError:
        print('That isn\'t a valid input for price. Please input a valid positive number.')
    if i == 9:
            print('This doesn\'t seem to be working, please try again later')
            sys.exit()
    i += 1

#leaves a space between lines on console
print('')

#checks number of people, try block incase somebody tries to give an incorrect input. Inside a while block to keep
#trying up to a max of 10 times
i = 0
while i < 10:
    #catch the error if there is one and loop back to retry input
    try:
        num_people = input("And how many people are there? ")
        #handles negative answers which shouldn't be given
        if int(num_people) > 0:
            num_people = int(num_people)
            break
        else:
            print('The number of people should be at least one or more')
    except ValueError:
        print('That isn\'t a valid input for a number of people. Please give a valid integer number')
    if i == 9:
            print('This doesn\'t seem to be working, please try again later')
            sys.exit()
    #increase the loop counter
    i += 1

#leaves a space between lines
print('')

#initialise array of correct tip amounts
tip_arr = [10, 15, 20]

#Get's the tip amount
tip_amount = 0

#Reinitialize loop counter to 0
i = 0

#Capture the input for the tip amount inside a while loop with a try block to catch errors
#This is to ensure an appropriate input
while tip_amount not in tip_arr:
    tip_amount = input('What percentage would you like to tip? 10, 15 or 20? ')
    try:
        tip_amount = int(tip_amount)
        if tip_amount not in tip_arr:
            print('That\'s not a valid option. Please enter an option from the list provided')
    except ValueError:
        print('That isn\'t a valid input for the tip. Please give a valid integer number from the list provided')
    if i == 9:
            print('This doesn\'t seem to be working, please try again later')
            sys.exit()
    i += 1

#leaves a space between lines
print('')

#Calculate and store the bill price and tip price per person
individual_bill = (bill_price/num_people)
individual_tip = individual_bill*(tip_amount/100)

#Prints total price and tip price per person
print(f'Each person should pay {individual_bill+individual_tip:.2f}')
print('')
print(f'This includes a bill price of {individual_bill:.2f}')
print('')
print(f'And a tip price of {individual_tip:.2f}')