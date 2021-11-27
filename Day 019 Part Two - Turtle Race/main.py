'''
Day 19 of 100 days of code python challenge - The purpose of todays project is in two parts with this being part two.
This part of the project is to make a turtle race using the python built in turtle library
'''
from turtle import Turtle, Screen
from tkinter import messagebox
import re
import sys
import random

def main():
    # Instantiate the screen
    screen = Screen()

    # Set the screen dimensions
    screen.setup(width=500, height=400)

    # Store which turtle the user is going to bet on, use a while loop to get an appropriate 
    counter = 10
    input_flag = False 
    while counter and not input_flag:
        # Get which turtle the user is going to bet on
        turtle_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color from red, orange, yellow, green, blue, indigo or violet: ")
        # Using regex to get a valid input

        # Each of these blocks is essentially the same - it tries to match one of the colours and if it does then it
        # normalizes the input for later comparison and flips the input flag so that the while loop breaks
        if re.compile("[Rr][Ee][Dd]").fullmatch(turtle_bet):
            turtle_bet = "red"
            input_flag = True
        elif re.compile("[Oo][Rr][Aa][Nn][Gg][Ee]").fullmatch(turtle_bet):
            turtle_bet = "orange"
            input_flag = True
        elif re.compile("[Yy][Ee][Ll][Ll][Oo][Ww]").fullmatch(turtle_bet):
            turtle_bet = "yellow"
            input_flag = True
        elif re.compile("[Gg][Rr][Ee][Ee][Nn]").fullmatch(turtle_bet):
            turtle_bet = "green"
            input_flag = True
        elif re.compile("[Bb][Ll][Uu][Ee]").fullmatch(turtle_bet):
            turtle_bet = "blue"
            input_flag = True
        elif re.compile("[Ii][Nn][Dd][Ii][Gg][Oo]").fullmatch(turtle_bet):
            turtle_bet = "indigo"
            input_flag = True
        elif re.compile("[Vv][Ii][Oo][Ll][Ee][Tt]").fullmatch(turtle_bet):
            turtle_bet = "violet"
            input_flag = True
        # If the user gives an invalid input then reduce the counter and give an error message
        else:
            counter -= 1
            if not counter:
                # If the user gives too many incorrect inputs then show a final error message before exiting
                messagebox.showerror(title="Too Many Invalid Inputs", message="You have given too many incorrect inputs, the system will now exit")
                sys.exit()
            # If the user gives an incorrect input then show an error message
            messagebox.showerror(title="Wrong Input", message="Please enter a valid input, red, orange, yellow, green, blue, indigo, violet")

    # Make a list to store all of the turtles in, as well as a colour list
    turtle_list = []
    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    # Instantiate the turtles and add them to the turtle list
    red = Turtle()
    turtle_list.append(red)
    orange = Turtle()
    turtle_list.append(orange)
    yellow = Turtle()
    turtle_list.append(yellow)
    green = Turtle()
    turtle_list.append(green)
    blue = Turtle()
    turtle_list.append(blue)
    indigo = Turtle()
    turtle_list.append(indigo)
    violet = Turtle()
    turtle_list.append(violet)

    # Set all the turtle colours by enumerating through them and picking from the colour list, also set their shapes
    for counter, turtle in enumerate(turtle_list):
        # Make sure they're the right colour
        turtle.color(color_list[counter])
        # Make sure they're the right shape
        turtle.shape("turtle")

    # Set all the turtles to the starting line
    for counter, turtle in enumerate(turtle_list):
        # Pen up otherwise it will draw lines to starting positions
        turtle.penup()
        # Send them to starting positions
        turtle.goto(x=-225, y=(counter*54)-160)

    def move_forward(turtle):
        '''This function moves one of the turtles forwards a random amount'''
        # Set a random amount to move
        pace = random.randint(5, 15)
        # Move the turtle forwards that amount
        turtle.forward(pace)

    # Make a while loop to keep moving the turtles until one of them reaches the finish
    input_flag = False
    while not input_flag:
        for turtle in turtle_list:
            # Move forward each turtle a little bit
            move_forward(turtle)
        for turtle in turtle_list:
            # Check each turtle to see if one of them has reached the end
            if round(turtle.xcor()) > 220:
                # If there is a winning turtle save it to the winning turtle variable and set the input flag to break out of the loop
                winning_turtle = turtle.color()[0]
                input_flag = True

    # Get the winning turtle as a string for comparison
    winning_turtle = f"{winning_turtle}".capitalize()

    # Check to see if the winning turtle was the one bet and give the appropriate message
    if turtle_bet.capitalize() == winning_turtle:
        messagebox.showinfo(title="You Won!", message=f'''{winning_turtle} was the winner.\nCongratulations your turtle won! Thanks for playing!''')
        sys.exit()
    else:
        messagebox.showinfo(title="You Lost!", message=f'''{winning_turtle} was the winner.\nSadly your turtle didn't win! Thanks for playing!''')
        sys.exit()

# This just ensures that the program only runs if its being run as a main instance
if __name__ == '__main__':
    main()