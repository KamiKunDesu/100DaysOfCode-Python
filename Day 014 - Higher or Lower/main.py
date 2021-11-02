'''
Day 14 of 100 days of code python challenge - The purpose of this project is to make a higher or lower game
which continuously compares instagram accounts against each other and you have to the player has to choose
which one has the most followers, they keep going until they get one wrong and the amount they got correct
is their score
'''
from game_data import data
from art import logo, vs
import time
import sys
import re
import random
import os

def clear(): os.system("clear")

def get_people_to_compare(data, personA=None, personB=None):
    '''This function gets the two people being compared, it sets A and B randomly on the first round,
    and then sets A to B and B randomly in all subsequent rounds'''

    if personA and personB:
        personA = personB
    else:
        personA = random.choice(data)
    # The while loop ensures that personA and personB are not the same
    personB = random.choice(data)
    while personA == personB:
        personB = random.choice(data)
    return personA, personB

def display_person(person):
    '''This function takes a person object and displays their stats to the screen'''

    return f"{person['name']} a {person['description']} from {person['country']}"

def main():
    '''This is the main function where the game is played'''

    # Set up the initial variables
    personA, personB = get_people_to_compare(data=data)
    player_life = True
    player_score = 0

    # The game is going to be played in a while loop which keeps going until the player gets a wrong answer
    # The console will clear and reprint each round
    while player_life:
        clear()

        # This block prints out the console for the player to decide on
        print(logo)
        print("Account A: " + display_person(personA))
        time.sleep(1)
        print(vs)
        time.sleep(1)
        print("Account B: " + display_person(personB))
        time.sleep(1)

        # This while block (so that we get a correct input) gets the input of the user
        counter = 10
        input_flag = False
        while counter and not input_flag:
            user_guess = input("Which account has more followers, A or B?: ")
            time.sleep(1)
            
            # using regex to check for a valid input
            if re.compile("[AaBb]").fullmatch(user_guess):
                
                # gets a standard response for ease of use
                if re.compile("[Aa]").fullmatch(user_guess):
                    user_guess = 'A'
                else:
                    user_guess = 'B'
                input_flag = True
            
            # handling an invalid input
            else:
                counter -= 1
                if not counter:
                    print("Sorry, you gave too many wrong inputs, the game will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please give a valid input, type 'A' or 'B'")
                time.sleep(1)
        
        # Handle whether the player won or not
        if user_guess == 'A':
            # Increment player score if they got it right
            if personA['follower_count'] > personB["follower_count"]: 
                print(f"That's right, {personA['name']} has {personA['follower_count']}m followers")
                print(f"and {personB['name']} has {personB['follower_count']}m followers!")
                player_score += 1
            # Otherwise set the player flag to false to break out of the loop
            else:
                print(f"Oh no that's wrong, {personA['name']} has {personA['follower_count']}m followers")
                print(f"and {personB['name']} has {personB['follower_count']}m followers!")
                player_life = False
        # Same logic as above but reversed for choosing B
        else:
            if personB['follower_count'] > personA["follower_count"]: 
                print(f"That's right, {personA['name']} has {personA['follower_count']}m followers")
                print(f"and {personB['name']} has {personB['follower_count']}m followers!")
                player_score += 1
                time.sleep(1)
            else:
                print(f"Oh no that's wrong, {personA['name']} has {personA['follower_count']}m followers")
                print(f"and {personB['name']} has {personB['follower_count']}m followers!")
                time.sleep(1)
                player_life = False

        # Update the people being compared
        personA, personB = get_people_to_compare(data=data, personA=personA, personB=personB)

    # Print the end of the game    
    print(f"You ended up with a score of {player_score}. Make sure to play again")
    time.sleep(4)
    sys.exit()

if __name__ == "__main__":
    main()







