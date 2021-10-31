'''
Day 11 of 100 days of code python challenge - The purpose of this capstone project is to make a blackjack program
which should be able to simulate an actual blackjack game.
'''
from dealer import Dealer
from player import Player



def main():
    '''The main function which runs the program'''
    
    # Substantiate the player and the dealer
    player = Player()
    dealer = Dealer()

    # Print the intro to the game
    print('''
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                           _/ |                
                          |__/                 
    ''')
    print('''
     _____
    |A .  | _____
    | /.\ ||A ^  | _____
    |(_._)|| / \ ||A _  | _____
    |  |  || \ / || ( ) ||A_ _ |
    |____V||  .  ||(_'_)||( v )|
           |____V||  |  || \ / |
                  |____V||  .  |
                         |____V|
    ''')

    # The main game
    dealer.show_initial_cards()
    player.show_all_cards()
    while player.keep_playing and not player.bust_status:
        player.hit_or_hold()
    
    # The results
    if player.bust_status:
        print("Unlucky you went bust! The dealer wins")
    else:
        dealer.show_all_cards()
        while dealer.current_score <= 16:
            dealer.draw_more_if_16()
        if dealer.bust_status:
            print("The dealer went bust, you win!")
        else:
            print(f"Your score is {player.current_score} and the dealer's is {dealer.current_score}.")
            if player.current_score > dealer.current_score:
                print("Congratulations you win!")
            else:
                print("Oh no the dealer won!")

if __name__ == "__main__":
    main()
