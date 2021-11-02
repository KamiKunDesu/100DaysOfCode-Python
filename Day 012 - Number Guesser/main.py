'''
Day 11 of 100 days of code python challenge - The purpose of this project is to make a higher or lower game
which randomly picks a number and gets the user to guess, only telling them whether they were correct, too high,
or too low.
'''
from number_guesser import NumberGuesser
import time

def main():
    '''This is the main function which handles the program'''

    # Print all of the introductory garble
    print("Welcome to higher or lower, the objective of the game is to guess the number I'm thinking of.")
    time.sleep(1.5)
    print("I'll tell you if your guess is correct, or if the number I'm thinking of is higher, or lower.")
    time.sleep(1.5)
    print("Try to guess the number I'm thinking of before you run out of lives.")
    time.sleep(1.5)
    number_guesser = NumberGuesser()
    number_guesser.play_game()


if __name__ == "__main__":
    main()