'''
The purpose of this document is to set up all the necessary functions required to be used in the main program
'''


# This assigns a goodness score to each letter derived from the probability that a letter appears in any given English Sentence
letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202,
                  0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193,
                  0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
                  ]

# This is an encoder function
def Encoder(string, S):
    Encoded_String = ""
    for s in string:
        #store the ascii representation of the lowercase version of the letter
        char = ord(s.lower())
        #basically if the ascii character wasn't alpha then skip
        if char not in range(97, 123):
            char = char
        #If it is alpha do the shit
        else:
            for i in range(0, S):
                #if get to top of the character list then restart (from z back to a basically)
                if char == 122:
                    char = 96
                char += 1
        #turn it back into a character and append it to the string
        char = chr(char)
        Encoded_String += char
    return Encoded_String

#this function can decode the message, the logic is the exact same as the encoder function but in reverse
def Decoder(string, S):
    Decoded_String = ""
    #logic below exactly the same as the encoder function
    for s in string:
        char = ord(s.lower())
        if char not in range(97, 123):
            char = char
        else:
            #this part is different because instead of approaching top of character list we bottom out and go from a back to z
            for i in range(0, S):
                if char == 97:
                    char = 123
                char -= 1
        char = chr(char)
        Decoded_String += char
    return Decoded_String

#This function checks the total goodness score of a given decode attempt
def Total_Goodness_Check(string):
    #Keep a track of the total goodness score of the string
    Total_Goodness = 0
    #check each letter in the string
    for letter in string:
        char = ord(letter.lower())
        #if its not alpha, then skip over it
        if char not in range(97, 123):
            char = char
        #else if it is alpha then check it's position in the goodness list and add the total goodness score of
        #that letter to the overall goodness score
        else:
            #because the representation of a starts at 97, bring it back to 0 so that a is index 0 in the goodness list
            char -= 97
            goodness_value = letterGoodness[char]
            Total_Goodness += goodness_value
    return Total_Goodness

#This function checks the goodness score for the message decoded in all possible shifts and stores them in an array
def All_Shift_Check(string):
    #The array to store the goodness scores for each of the different shifts
    Goodness_Test = []
    #for each possible shift
    for i in range(0, 27):
        #First make the decoded message with the current shift
        Decoded_Message = Decoder(string, i)
        #Work out the goodness score for this decoding
        Message_Goodness = Total_Goodness_Check(Decoded_Message)
        #Throw it in an array
        Goodness_Test.append(Message_Goodness)
    return Goodness_Test

#This function works out the best shift to decode a message that has been shift encoded
def Best_Choice(string):
    #Kind of self explanatory but store a list of goodness scores for each possible shift
    #Then store the index of the best score in shift (as this will be the shift)
    #Then decode the message using the best shift, and return that
    Goodness_Test = All_Shift_Check(string)
    Shift = Goodness_Test.index(max(Goodness_Test))
    Best_Choice = Decoder(string, Shift)
    return Best_Choice
