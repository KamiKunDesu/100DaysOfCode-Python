'''
Day 9 - The purpose of this project is to make a secret auction program, basically a program where you can
pass the computer around in a group and each of you can enter a bid for something, each time the console
will clear so no one knows what anyone else bid - at the end the max bid is calculated and the highest bidder
is announced
'''
import sys
import time
import os
import re

#store some ascii art for the program
gavel = '''
   ___________
   \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\
   `'-------'`
 .-------------.
/_______________\
'''

# A quick lambda function to clear the screen when necessary
def clear(): os.system("clear")

# This function gets a name
def get_name():
        # Since the screen clears for every new bidder do intro text each time
        # intro
        print(gavel)
        print("Welcome to the Secret Auction")

        # A very simple function that just gets the name
        name = input("What is your name?: ")
        return name
        

# This function gets the bid
def get_bid():
    # We'll use a while loop to make sure the user gives a positive integer, but we'll cap it at 10 to avoid overflow
    counter = 10
    while counter:
        # Try except block helps us ensure that we are getting an integer input
        try:
            bid_amount = int(input("How much are you going to bid? £ "))
        except ValueError:
            counter -= 1
            # Exit program if too many failed attempts
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            # Give a warning if the user gives a non int amount
            print("Please give a valid positive integer input")
            time.sleep(3)
            continue
        if bid_amount < 0:
            counter -= 1
            # Exit program if too many failed attempts
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            # Give a warning if they give a negative amount
            print("Please put a positive amount, you can't pay with negative cash")
            time.sleep(3)
            continue
        return bid_amount
        

# This function stores the name and bid of a person and returns it to a dictionary
def store_name_and_bid(bid_dictionary):
    # Get name and bid amount
    name = get_name()
    bid_amount = get_bid()
    bid_dictionary[name] = bid_amount
    return bid_dictionary 

# This function determines the max bidder
def determine_max_bidder(bid_dictionary):
    #Calculates and returns the max bidder and amount they paid
    max_name = ''
    max_bid = 0
    # A for loop to check and update the max bidder and max name
    for name, bid in bid_dictionary.items():
        if bid > max_bid:
            max_name = name
            max_bid = bid
    return [max_name, max_bid]

# A quick function to check if there's any more bidders
def more_bidders():
    # Initiate a counter and put a while block in to get a valid input
    counter = 10
    while counter > 0:
        more_bidders = input("Are there any more bidders? ")
        # Check if input something like Yes, returns false to keep the while block in main func going
        if re.compile('[Yy](es|ES)?').fullmatch(more_bidders):
            return False
         # Check if input something like No, returns true to break the while block in the main func
        elif re.compile('[Nn](o|O)?').fullmatch(more_bidders):
            return True
        # If not valid input reduce counter and restart while loop, if counter is 0 exit
        else:
            counter -= 1
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(3)
                sys.exit()
            print("Please give a valid input - 'Yes' or 'No'")

# A main function to bring the program together
def main():
    # Make a bid dictionary to keep it as a local variable for the whole function
    bid_dictionary = {}
    #Make a flag and counter for the while loops
    all_bidders_bid = False
    counter = 0
    while not all_bidders_bid and counter <= 1000:
        bid_dictionary = store_name_and_bid(bid_dictionary)
        counter += 1
        all_bidders_bid = more_bidders()
        clear()
    
    # Calculate and show max bidder
    max_bidder = determine_max_bidder(bid_dictionary)

    #Give result
    print(f"The highest bidder is {max_bidder[0]} who bid £{max_bidder[1]}")

#Call main if running as a script
if __name__ == "__main__":
    main()