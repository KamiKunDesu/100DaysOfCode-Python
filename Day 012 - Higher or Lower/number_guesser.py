'''This is the number guesser class for use in the higher or lower game'''
import random
import time
import sys
import re

class NumberGuesser:
    '''The number guesser class for the higher or lower game'''

    def __init__(self):
        '''The initialization method for the number guesser class'''

        self.number = random.randint(0, 100)
        self.difficulty_mode = self.easy_or_hard()

    def easy_or_hard(self):
        '''This function decides whether the user is on easy or hard mode'''
        
        counter = 10
        while counter >= 0:
            difficulty_mode = input("Would you prefer easy or hard mode: ")
            time.sleep(1.5)
            # Check if input something like easy and return easy
            if re.compile('[Ee][Aa][Ss][Yy]').fullmatch(difficulty_mode):
                return "Easy"
            # Check if input something like hard and return hard
            elif re.compile('[Hh][Aa][Rr][Dd]').fullmatch(difficulty_mode):
                return "Hard"
            # If not valid input reduce counter and restart while loop, if counter is 0 exit
            else:
                counter -= 1
                if counter == 0:
                    print("You have failed too many times. Program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please give a valid input - 'Easy' or 'Hard'")
                time.sleep(1.5)
    
    def play_game(self):
        '''This function handles the actual game'''
        # Set up game lives and also a counter incase of too many wrong inputs
        # Also a win flag in case the user guesses correctly
        game_lives = self.get_game_lives()
        counter = 10
        win_flag = False
        while game_lives and counter and not win_flag:
            #Tell user how many lives they have left
            print(f"You currently have {game_lives} lives")
            time.sleep(1.5)
            # Try except block to get valid integer input
            try:
                guess = int(input("What number would you like to guess?: "))
                time.sleep(1.5)
                # Trip the win flag if they guess right, tell them they were wrong if not
                if guess == self.number:
                    win_flag = True
                else:
                    # Handle if the number is higher or lower
                    if guess > self.number:
                        print("Nope, the correct number is lower than that")
                        game_lives -= 1
                        time.sleep(1.5)
                    else:
                        print("Nope, the correct number is higher than that")
                        game_lives -= 1
                        time.sleep(1.5)
            except ValueError:
                counter -= 1
                if not counter:
                    print("You have failed too many times. Program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please guess a valid integer number")
                time.sleep(1.5)

        # Print the final result if it's a win or a loss
        if win_flag == True:
            print(f"Congratulations you guessed {self.number} which is correct! You win, make sure to play again")
            time.sleep(5)
            sys.exit()
        else:
            print(f"Oh no you ran out of lives, the correct number was {self.number} make sure to play again")
            time.sleep(5)
            sys.exit()
        
    def get_game_lives(self):
        '''This function returns the game lives based on difficulty mode'''
        return 10 if self.difficulty_mode == "Easy" else 5

# number = NumberGuesser()
# number.play_game()
        
        
        
