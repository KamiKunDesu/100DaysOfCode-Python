'''Day 26 of 100 days of code python challenge - The purpose of todays project is to make a program which takes an input
from the user and returns a list of the NATO alphabet equivalents
'''
import pandas as pd

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def main():
    '''Put the program in a main function so that it only runs if we run as a script'''

    # First let's get the csv into a dataframe
    nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
    # Then let's loop through it to get it in a dictionary
    nato_dict = {row.letter:row.code for index, row in nato_data.iterrows()}

    # Get the user input
    user_input = input("What do you need to make into the Nato alphabet? ")
    # Make a list of the nato chars
    return_list = [nato_dict[char] for char in user_input.upper() if char in nato_dict]
    # Then print the list
    print(return_list)

if __name__ == "__main__":
    main()

