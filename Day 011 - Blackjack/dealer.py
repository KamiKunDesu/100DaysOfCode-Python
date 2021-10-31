'''
This doc is to set up the dealer class for the game
'''
from blackjack_player import BlackjackPlayer

class Dealer(BlackjackPlayer):
    '''This is the dealer class that the player plays against'''
    
    def show_initial_cards(self):
        '''This function shows the initial cards of the Dealer'''
        print(f"The dealer starts with [{self.current_cards[0]}, ?]")

    def show_all_cards(self):
        '''This function shows all cards of the dealer'''
        print(f"The dealer has the cards {self.current_cards} which makes a score of {self.current_score}")

    def draw_more_if_16(self):
        '''This forces the dealer to draw one more card if they have 16 cards'''
        if self.current_score <= 16:
            print("The dealer has less a score of less than 16, they have to draw another card")
            self.draw_card()
            self.show_all_cards()

