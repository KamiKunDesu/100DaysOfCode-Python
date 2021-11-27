'''
Day 19 of 100 days of code python challenge - The purpose of todays project is in two parts with this being part one.
This part of the project is to make an etch a sketch app using the python built in turtle library
'''
from turtle import Turtle, Screen

controller = Turtle()
screen = Screen()

def move_forwards():
    '''This function moves the pen forward'''
    controller.forward(5)

def move_backwards():
    '''This function moves the pen backward'''
    controller.backward(5)

def turn_right():
    '''This function turns the pen direction left'''
    controller.setheading(controller.heading()-5)

def turn_left():
    '''This function turns the pen direction right'''
    controller.setheading(controller.heading()+5)

def clear():
    '''This function clears the screen and brings the pen back to the centre'''
    controller.clear()
    controller.penup()
    controller.home()
    controller.pendown()

# Make the screen listen and assign the different listeners
screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=clear)


screen.exitonclick()