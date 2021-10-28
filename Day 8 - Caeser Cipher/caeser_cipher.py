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
        char = ord(s.lower())
        if char not in range(97, 123):
            char = char
        else:
            for i in range(0, S):
                if char == 122:
                    char = 96
                char += 1
        char = chr(char)
        Encoded_String += char
    return Encoded_String


def Decoder(string, S):
    Decoded_String = ""
    for s in string:
        char = ord(s.lower())
        if char not in range(97, 123):
            char = char
        else:
            for i in range(0, S):
                if char == 97:
                    char = 123
                char -= 1
        char = chr(char)
        Decoded_String += char
    return Decoded_String


def Total_Goodness_Check(string):
    Total_Goodness = 0
    for letter in string:
        char = ord(letter)
        if char == 32:
            char = char
        else:
            char -= 65
            goodness_value = letterGoodness[char]
            Total_Goodness += goodness_value
    return Total_Goodness


def All_Shift_Check(string):
    Goodness_Test = []
    inputvar = string
    for i in range(0, 27):
        Decoded_Message = Decoder(inputvar, i)
        Message_Goodness = Total_Goodness_Check(Decoded_Message)
        Goodness_Test.append(Message_Goodness)
    return Goodness_Test


def Best_Choice(string):
    Goodness_Test = All_Shift_Check(string)
    Shift = Goodness_Test.index(max(Goodness_Test))
    Best_Choice = Decoder(string, Shift)
    return Best_Choice

print(Encoder("XyZ", 1))