'''
Day 4 of 100 of the 100 days of code python challenge - The purpose of this day 4 project is to build a rock paper
scissors game that uses randomization to allow you to play games of rock paper scissors against the computer 
'''
import random
import sys
import time

#store ASCII art for rock, paper and scissors
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#initiate options array
choices = [rock, paper, scissors]

#initiate while loop which will ask the user for their choice until valid input given or 10 attempts reached
counter = 0
while counter < 10:
    #get user choice
    user_input = input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: ')
    #break out the loop if valid input
    if user_input in ['0', '1', '2']:
        break
    counter += 1
    #if the max counter reached - exit the program with an exit message
    if counter == 10:
        print('This doesn\'t appear to be working right now, please try again')
        time.sleep(5)
        sys.exit()
    #re explain the valid input options to the user
    print('That wasn\'t a valid input. Please input either 0, 1 or 2 with no spaces.')

#convert user input to int
user_input = int(user_input)

#choose computer input
computer_input = random.randint(0,2)

#store both user choice and computer choice
user_choice = choices[user_input]
computer_choice = choices[computer_input]

#control flow for handling different game outcomes but also preamble printed upfront to avoid redundant code reuse
print('You chose:')
time.sleep(1)
print(user_choice)
time.sleep(1)
print('And the computer chose:')
time.sleep(1)
print(computer_choice)
time.sleep(1)
#in case of a draw
if user_choice == computer_choice:
    print('Looks like it was a Draw!')
#handle the losing cases
elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 0):
    print('Oh no looks like you lost!')
#handle the winning clauses
elif (user_input == 0 and computer_input == 2) or (user_input == 1 and computer_input == 0) or (user_input == 2 and computer_input == 1):
    print('CONGRATS! You won!')
