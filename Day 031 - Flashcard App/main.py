'''Day 031- The purpose of this project is to bring together all the knowledge learned about Tkinter so far in
making a flash card application. The app itself should be able to store cards and allow them to be reviewed'''

from tkinter import *
import random
import pandas as pd

#----------------- READING CSV DATA INTO DATAFRAME -------------------- #

# Firstly read the data into a dataframe from the csv
try:
    words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pd.read_csv("data/french_words.csv")
# Then store it in a dictionary
words_dict_list = words_data.to_dict(orient="records")

#---------- INITIALISING A VARIABLE TO STORE WORD CHOICE GLOBALLY ----- #

# First get a random word pair from the list
select_word = {}

# ---------------------------- FUNCTIONS ------------------------------ #

# First lets set up the function to randomize the word on the flashcard
def next_card():
    '''This function selects a random French word from the list for use as
    as a flashcard'''
    # First global the variables necessary
    global select_word, flip_timer
    # Cancel any previous timer
    window.after_cancel(flip_timer)
    # First get a random word pair from the list
    select_word = words_dict_list[random.randint(0, len(words_dict_list)-1)]
    # Then store the French part of the word
    french_word = select_word["French"]
    # Then make sure that the image is the front card image
    canvas.itemconfig(curr_image, image=flashcard_front)
    # Then set the word to the selected word, and the title
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    # Reset the flip timer variable for window.after()
    flip_timer = window.after(ms=3000, func=turn_card)

def turn_card():
    '''This command will be used to turn the card to the back card'''
    # First lets config the image to the back card
    canvas.itemconfig(curr_image, image=flashcard_back)
    # Then reconfigure the text to be the English word and white.
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=select_word["English"], fill="white")

def is_known():
    '''This function handles the case where he user clicks the card known button,
    it flips to the next card but also makes a known words list'''
    # First remove the current card from the overall list
    words_dict_list.remove(select_word)
    # Then create a new dataframe of the now current list
    data = pd.DataFrame(words_dict_list)
    # Then save it as a new CSV file
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# Set up a window
window = Tk()
# Set the title
window.title("Flashy")
# Add some padding to the window and set the background colour
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Then after 3 seconds has passed turn the card
flip_timer = window.after(ms=3000, func=turn_card)

# Create the card image on a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# First load in the image for the front card and the back card
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
# Then add the idea of a card onto the canvas, setting it first to front card, and storing it in a variable for manipulation
curr_image = canvas.create_image(400, 263, image=flashcard_front)
# Add text onto the canvas and store it in a variable for both elements, also set the text to the correct params
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# Finally pack the canvas onto the main window
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
# First load in the images
correct_image = PhotoImage(file="images/right.png")
incorrect_image = PhotoImage(file="images/wrong.png")
# Then make the buttons
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_card)
# Finally pack them into the window
correct_button.grid(column=0, row=1)
incorrect_button.grid(column=1,row=1)

next_card()

window.mainloop()