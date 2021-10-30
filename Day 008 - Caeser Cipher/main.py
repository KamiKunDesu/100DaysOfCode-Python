'''
Day 8 of 100 days of code python challenge - The purpose of this project is to make a program which can encode and decode messages using a caeser cipher.
I'm going to take it a step further by making it possible to decode a message encoded with the caeser cipher,
even if you don't know the shift.
'''
import caeser_cipher as cipher
import time
import re
import sys

# Encode function, the beginning logic will be the exact same as the decode_known function so the comments apply
# there as well for the first two checks
def encode():
    # while loop will keep trying to get input, but has a counter to avoid infinite loop
    counter = 10
    while counter > 0:
        # This try block gets the user input and tries to convert it to an int raising a value error if not and also
        # decreasing the counter to avoid an infinite loop, it exits the program promptly if you fail to input too many times
        try:
            shift_index = int(input("What shift would you like to use? "))
            time.sleep(1.5)
        except ValueError:
            counter -= 1
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            print("Please input a valid positive integer")
            time.sleep(1)
            continue

        # Next let's check that the user gave a positive shift
        if shift_index < 0:
            counter -= 1
            # Check if counter has reached 0 and exit program if it has
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            print("Please use a positive integer not negative")
            time.sleep(1.5)
            continue

        # Now that checks are done lets encode the message
        message = input(
            "Please input the message that you would like to encode: ")
        encoded_message = cipher.Encoder(message, shift_index)
        time.sleep(1.5)
        print(f'Your encoded message is: {encoded_message}')
        return encoded_message

# Below is the decode_known function which handles when the user wants to decode a message and they know the shift
def decode_known():
    # while loop will keep trying to get input, but has a counter to avoid infinite loop
    counter = 10
    while counter > 0:
        # This try block gets the user input and tries to convert it to an int raising a value error if not and also
        # decreasing the counter to avoid an infinite loop, it exits the program promptly if you fail to input too many times
        try:
            shift_index = int(input("What shift would you like to use? "))
            time.sleep(1.5)
        except ValueError:
            counter -= 1
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            print("Please input a valid positive integer")
            time.sleep(1)
            continue

        # Next let's check that the user gave a positive shift
        if shift_index < 0:
            counter -= 1
            # Check if counter has reached 0 and exit program if it has
            if counter == 0:
                print("You have failed too many times. Program will now exit")
                time.sleep(4)
                sys.exit()
            print("Please use a positive integer not negative")
            time.sleep(1.5)
            continue

        # Now that checks are done lets decode the message
        message = input(
            "Please input the message that you would like to decode: ")
        decoded_message = cipher.Decoder(message, shift_index)
        time.sleep(1.5)
        print(f'Your decoded message is: {decoded_message}')
        return decoded_message

# The following function decodes the message even if you don't know what shift to use
def decode_unknown():
    # The logic is the same it just doesn't need to intake a shift
    message = input("Please input the message that you would like to decode ")
    decoded_message = cipher.Best_Choice(message)
    time.sleep(1.5)
    print(f'Your decoded message is: {decoded_message}')
    return decoded_message


# Main function
def main():
    counter_main = 10
    # Get user input
    while counter_main:
        user_input = input("Do you want to encode? or decode? ")
        time.sleep(1.5)
        # Check if user input something like encode
        if re.compile("[Ee][Nn][Cc][Oo][Dd][Ee]").fullmatch(user_input):
            # Run encode function and then sys exit
            encode()
            time.sleep(1.5)
            print("This message will self destruct in 10 seconds, make a note of the message quickly")
            time.sleep(10)
            print("")
            sys.exit()
        # Check if the user input something like Decode
        elif re.compile("[Dd][Ee][Cc][Oo][Dd][Ee]").fullmatch(user_input):
            # Start a while loop to get input about whether they know the the shift key or note
            inner_counter = 10
            while inner_counter:
                known_or_unknown = input("Do you know the shift? ")
                # Check if input something like Yes
                if re.compile('[Yy](es|ES)?').fullmatch(known_or_unknown):
                    # Run decode known function and then sys exit
                    decode_known()
                    print("This message will self destruct in 10 seconds, make a note of the message quickly")
                    time.sleep(10)
                    print("")
                    sys.exit()
                # Check if input something like No
                elif re.compile('[Nn](o|O)?').fullmatch(known_or_unknown):
                    # Run the decode unknown problem and then sys exit
                    decode_unknown()
                    print("This message will self destruct in 10 seconds, make a note of the message quickly")
                    time.sleep(10)
                    print("")
                    sys.exit()
                # If not valid input reduce counter and restart while loop, if counter is 0 exit
                else:
                    inner_counter -= 1
                    if not inner_counter:
                        print("Too many wrong inputs, program will now exit")
                        time.sleep(4)
                        sys.exit()
                    print("Please give a valid answer, Yes or No")
                    time.sleep(1.5)
        # If not valid input reduce counter and restart while loop, if counter is 0 exit
        else:
                    counter_main -= 1
                    if not counter_main:
                        print("Too many wrong inputs, program will now exit")
                        time.sleep(4)
                        sys.exit()
                    print("Please give a valid answer, Encode or Decode")
                    time.sleep(1.5)
                    print("")

if __name__ == '__main__':
    main()
