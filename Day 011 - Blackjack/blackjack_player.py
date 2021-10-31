'''
This document is the class that both the dealer and the player inherit from
'''
import random

class BlackjackPlayer:
    '''This class stores the methods and attributes of the blackjack player'''
    
    def __init__(self):
        '''The initialization function of the class'''
        self.possible_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.card_scores = {
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'J': 10,
                'Q': 10,
                'K': 10,
                'A': [1, 11]}

        self.current_cards = [random.choice(self.possible_cards), random.choice(self.possible_cards)]

        self.current_score = self.calculate_score()

        self.bust_status = self.bust()

    def calculate_score(self) -> int:
        '''This function calculates the score of the current cards held'''
            
        # First we need to calculate the score without any aces to see what the value of the ace should be
        # if there is one
        cards_without_ace = [card for card in self.current_cards if card != 'A']
        score = 0

        # First get the non-ace cards
        for card in cards_without_ace:
            score += self.card_scores[card]

        # Then add on the score of any aces 
        for card in self.current_cards:
            if card == 'A':
                if score + 11 <= 21:
                    score += self.card_scores[card][1]
                else:
                    score += self.card_scores[card][0]
            
        return score
            
    def draw_card(self):
        '''This function draws a card and adds it to the players current cards'''

        #Draw a card and then update the score
        self.current_cards.append(random.choice(self.possible_cards))
        self.current_score = self.calculate_score()
        self.bust_status = self.bust()
        
    def bust(self):
        '''This function makes the player go bust'''
            
        if self.current_score > 21:
            return True
        else:
            return False


     