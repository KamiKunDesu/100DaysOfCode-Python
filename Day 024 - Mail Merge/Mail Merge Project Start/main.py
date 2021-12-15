'''Day 24 of 100 days of code python challenge - The purpose of todays project is to make a program which can take a letter
template and a list of names and factory produce "personalised" letters to be sent out
'''
def main():
    '''The main function so that the program only runs if it's being run as a script'''

    # First read in the names from the list of names that we have
    with open("Input/Names/invited_names.txt", 'r') as names_file:
        names = names_file.readlines()

    # Strip the names of their \n aspect by enumerating through the list so we can edit it in place
    for counter, name in enumerate(names):
        names[counter] = name.replace("\n", "")
    
    # Then get the letter
    with open("Input/Letters/starting_letter.txt", 'r') as letter_file:
        letter = letter_file.read()

    # Now loop through the names, make the letters and save them
    for name in names:
        with open(f"Output/ReadyToSend/invite_to_{name}.txt", 'w') as ready_letter:
            ready_letter.write(letter.replace('[name]', name))

if __name__ == "__main__":
    main()