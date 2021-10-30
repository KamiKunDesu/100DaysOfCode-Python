'''
Day 7 of 100 days of code python challenge - The objective of Day 7 is to make a hangman game which generates a random 
word for the user to guess until they run out of lives, a digitization of the hangman game
'''
import random
import csv
import time
import sys

#bring in list of all words from the common words csv
with open('word_list.csv', 'r') as f:
    word_list = [word[0] for word in csv.reader(f) if word != []]

#Initializing all the stages of the hangman drawing and the title
hangman_lives_7 = ''
hangman_lives_6 = '''
 _______
 |/      
 |      
 |      
 |       
 |      
 |
_|___
'''
hangman_lives_5 = '''
 _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
_|___
'''
hangman_lives_4 = '''
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
'''
hangman_lives_3 = '''
  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |      
 |
_|___
'''
hangman_lives_2 = '''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      
 |
_|___
'''
hangman_lives_1 = '''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / 
 |
_|___
'''
hangman_lives_0 = '''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \
 |
_|___
'''
hangman_title = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
#Make an ascii asset list because it's useful
asset_list = [hangman_lives_0, hangman_lives_1, hangman_lives_2, hangman_lives_3, hangman_lives_4,
              hangman_lives_5, hangman_lives_6, hangman_lives_7, hangman_title
              ]

#get the target word randomly from the word list and also break it into a list for manipulating
target_word = word_list[random.randint(0, len(word_list)-1)]
target_word_arr = list(target_word)

#Make the string of blanks that will be shown to the user, and also make a list for manipulating
display_str = '_'*len(target_word)
display_str_arr = list(display_str)

#initialise player lives
player_lives = 7

#initialise a list to store previous guesses
guess_list = []

#making a function to update the string that gets shown to the user
def update_display_guess_letter(target_word_arr, guess_letter, display_str_arr):
    #make a list of indices where the guess letter is in the target word
    indices = [i for i, x in enumerate(target_word_arr) if x == guess_letter]
    #update the display_str_arr to replace blanks
    if indices:
        for index in indices:
            display_str_arr[index] = guess_letter
    return display_str_arr

#a function to handle the user trying to guess the whole word
def guess_whole_word(target_word, guess_word):
    return target_word == guess_word

#Quick function to print the right hangman image based on num of lives
def print_hangman(player_lives, asset_list):
    print(asset_list[player_lives])

#This function prints the display string
def print_display_str(display_str_arr):
    print(''.join(display_str_arr) + f' ({len(display_str_arr)} letters)')

#This function deals with checking if you already guessed that
def check_guess_list(guess_list, guess):
    if guess in guess_list:
        print("Bro you already guessed that")
        return True
    else:
        guess_list.append(guess)
        return False

#initiate a win-flag to check if player has won
win_flag = False

#print intro to game
print(hangman_title + "\n")
time.sleep(1)
print("Welcome to Hangman, the goal is to guess the word before we hang your little friend!\n")
time.sleep(1)
print("Good Luck!")

#A while loop to keep getting guesses until either player runs out of lives or wins
while player_lives and not win_flag:
    #print some things to show the current status of the game
    print_hangman(player_lives, asset_list)
    print_display_str(display_str_arr)
    print(f"You have already guessed {guess_list}")

    #Get user input
    user_guess = input("What is your guess? ")
    #check to make sure they're using letters
    if not user_guess.isalpha():
        time.sleep(1)
        print("please only guess a word or a letter")
        time.sleep(1)
        continue
    time.sleep(1)

    #Check if user already tried this
    if check_guess_list(guess_list, user_guess):
        time.sleep(1)
        continue

    #Handle if the guess was just a letter
    if len(user_guess) == 1:
        #so that can check if player made a wrong guess or not
        prev_display_str_arr = [char for char in display_str_arr]
        display_str_arr = update_display_guess_letter(target_word_arr, user_guess, display_str_arr)
        #if they made a wrong guess
        if prev_display_str_arr == display_str_arr:
            player_lives -= 1
            print("Nope... Try again!")
            time.sleep(1)
        #if their guess was correct
        else:
            print("Good job, that is in there!")
            if display_str_arr == target_word_arr:
                win_flag = True
            time.sleep(1)
    #Handle if the user tried to guess the whole word
    else:
        #check this word makes sense to guess
        if len(user_guess) != len(target_word):
            print("Maybe try guessing a word that's the same length as the target word dummy.")
            time.sleep(1)
        else:
            win_flag = guess_whole_word(target_word, user_guess)
            #if they get the guess right
            if win_flag:
                print("No way, you actually got it!")
                time.sleep(1)
            #if they didn't
            else:
                player_lives -= 1
                print("No shot buddy.")
                time.sleep(1)

#Either player has won or lost, run different scenario depending on
if win_flag:
    print("Congratulations you won! You saved you friend from the Hangman! Come play again!")
    time.sleep(4)
    sys.exit()
else:
    print_hangman(player_lives, asset_list)
    print("Oh no, looks like the hangman got your friend before you could save him! Come play again!")
    time.sleep(4)
    sys.exit()
