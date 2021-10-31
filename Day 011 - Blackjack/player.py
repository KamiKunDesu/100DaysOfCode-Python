'''This doc sets up up the player class for the game'''
from blackjack_player import BlackjackPlayer
import sys
import time
import re

class Player(BlackjackPlayer):
    '''This is the player class that the user will play as'''

    def __init__(self):
        '''This function extends the Blackjackplayer init and adds an extra attribute'''    
        super().__init__()
        self.keep_playing = True

    def show_all_cards(self):
        '''This function shows all cards of the player'''
        
        print(f"You currently have {self.current_cards} which makes a score of {self.current_score}")

    def hit_or_hold(self):
        '''This function decides whether or not the user is going to hit or hold'''
        
        counter = 10
        while counter >= 0:
            player_hit_or_hold = input("Would you like to draw another card?: ")
            if re.compile('[Yy](es|ES)?').fullmatch(player_hit_or_hold):
                print("HIT ME!")
                self.draw_card()
                self.show_all_cards()
                break
            # Check if input something like No, returns true to break the while block in the main func
            elif re.compile('[Nn](o|O)?').fullmatch(player_hit_or_hold):
                print("I think I'll hold")
                self.keep_playing = False
                break
            # If not valid input reduce counter and restart while loop, if counter is 0 exit
            else:
                counter -= 1
                if counter == 0:
                    print("You have failed too many times. Program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please give a valid input - 'Yes' or 'No'")


    


    