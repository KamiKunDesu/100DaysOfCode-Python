'''
Day 5 of the 100 days of code python challenge - The objective of day 5 is to make a strong password generator which
can take in the amount of letters, numbers and symbols that you want and generates a strong random password
'''
import random
import sys
import time

#first initialise the lists of letters, numbers and passwords, first two lists of numbers and letters generated using a list comprehension
letters = sorted([chr(num) for num in range(97,123)] + [chr(num) for num in range(65,91)])
numbers = [str(num) for num in range(0,10)]
symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<',',','>','.','?','/']

'''
We're going to be getting the amount of letters, numbers and symbols that the user needs in their password.
This will all happen inside of a while block, the reason being that at the end there is going to be a check that the
total length of the password is within the minimum and maximum bounds of password length, and if it isn't, then it's going
to go through the process again to make sure the password generated is an appropriate length.
'''

while True:

    #This while block gets the letter count
    while True:
        letter_count = input('how many letters should your password have? ')
        #A try block to check if valid integer input and handle exception if not
        try:
            letter_count = int(letter_count)
            if letter_count in range(1,129):
                break
            else:
                print('That wasn\'t a valid input, please give an integer value between 1 and 128')
        except ValueError:
            print('This was not a valid input, please input an integer value between 1 and 128')

    #Same block as above but for numbers
    while True:
        num_count = input('how many numbers should your password have? ')
        try:
            num_count = int(num_count)
            if num_count in range(1,129):
                break
            else:
                print('That wasn\'t a valid input, please give an integer value between 1 and 128')
        except ValueError:
            print('This was not a valid input, please input an integer value between 1 and 128')

    #Same block but for symbols
    while True:
        symbol_count = input('how many symbols should your password have? ')
        try:
            symbol_count = int(symbol_count)
            if symbol_count in range(1,129):
                break
            else:
                print('That wasn\'t a valid input, please give an integer value between 1 and 128')
        except ValueError:
            print('This was not a valid input, please input an integer value between 1 and 128')

    #Now use this same logic as the block above to get the minimum length of the password
    while True:
        min_count = input('What is the minimum length of the password? ')
        try:
            min_count = int(min_count)
            if min_count in range(1,129):
                break
            else:
                print('That wasn\'t a valid input, please give an integer value between 1 and 128')
        except ValueError:
            print('This was not a valid input, please input an integer value between 1 and 128')

    #And use the same logic to get the maximum length of the password, with an extra check to ensure that the maximum
    #length of the password is greater than the minimum length of the password.
    while True:
        max_count = input('What is the maximum length of the password? ')
        try:
            max_count = int(max_count)
            if max_count in range(1,129) and max_count >= min_count:
                break
            elif max_count in range(1,129) and max_count < min_count:
                print('You can\'t have a maximum password length shorter than the minimum length')
            else:
                print('That wasn\'t a valid input, please give an integer value between 1 and 128')
        except ValueError:
            print('This was not a valid input, please input an integer value between 1 and 128')

    #A quick check to see that the total number of symbols, numbers and letters doesn't exceed 128
    total_count = num_count + letter_count + symbol_count
    if total_count > max_count:
        print(f'The number of characters exceeds the max limit, the number or letters, numbers and symbols totalled should not exceed the maximum password limit of {max_count}')
    elif total_count < min_count:
        print(f'The number of characters is not enough, the number or letters, numbers and symbols totalled should be greater than the minimum password length of {min_count}')
    else:
        break

#initialise an array to store out final password
password = []

#add the letters to array
for i in range(letter_count):
    #loop through and append a random letter from letters to the password until the letter count has been reached
    password.append(letters[random.randint(0,len(letters)-1)])

#add the numbers to the array using the same logic as above
for i in range(num_count):
    password.append(numbers[random.randint(0,len(numbers)-1)])

#finally add symbols to the array using the same logic as above
for i in range(symbol_count):
    password.append(symbols[random.randint(0,len(symbols)-1)])

#now randomize the final array so that the selected items appear in a random order
random.shuffle(password)

#finally change the array into a string
password = ''.join(password)

#and return the password to the user
print('We have generated the following password for you, take note of it within the next 60 seconds before the program exits')
print(password)

#Lastly, exit the program after waiting 60 seconds for the user to note down the passwords
time.sleep(60)
sys.exit()