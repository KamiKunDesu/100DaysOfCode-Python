'''
Day 18 of 100 days of code python challenge - The purpose of todays project is to get used to turtle
and generally start to learn about GUIs in python. The name of the project is in reference to a painting by
Hirst of evenly spaced dots which sold for $1.75m - it's kind of a joke but that's what we'll reproduce with
the turtle module
'''
from turtle import Turtle, Screen
import random
import colorgram


def main():
    '''This is the main function which will run if in the main namespace'''
    # Extract the colours from the Hirst example to get his colour pallet - I had to give a relative path because running
    # the program from the main repository in vs code - for others the path will need to be adjusted as necessary
    colors = colorgram.extract('./Day 018 - Million Dollar Painting/hirst_dot.jpg', 60)

    # Initialise an empty list to store the colours in
    color_list = []

    # Loop through the color object and make a tuple with rgb values to append to the list for each extracted colour
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_list.append(new_color)

    # Substantiate a screen and set it up
    screen = Screen()
    screen.setup(width=500, height=500)
    screen.colormode(255)

    # Substantiate a turtle to draw the picture, set it's initial parameters
    tirstle = Turtle()
    tirstle.speed(0.5)
    tirstle.penup()
    tirstle.setx(-225)
    tirstle.sety(-225)
    tirstle.pensize(25)

    def draw_across():
        '''This function draws 10 dots across the screen choosing a random colour from the colour pallet for each
        dot'''
        # Loop for each dot
        for i in range(10):
            # Put the pen down
            tirstle.pendown()
            # Draw the dot with a random colour
            tirstle.dot(25, random.choice(color_list))
            # Bring the pen up
            tirstle.penup()
            # Move along to the next position
            tirstle.forward(50)

    def move_up(line):
        '''This function moves up to the beginning of the next line'''
        # Depending on which vertical line we're on set the vertical position
        tirstle.sety(-225+(line*50))
        # Reset x position to the beginning 
        tirstle.setx(-225)

    # Generates the function
    for i in range(10):
        draw_across()
        move_up(i+1)

    screen.exitonclick()

if __name__ == "__main__":
    main()


