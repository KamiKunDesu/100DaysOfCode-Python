'''
This is one of the turtle challenges that I had to complete - I made some art with it, I call this: "4th Dimensional Flower"
'''
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


turtle = Turtle()
turtle.shape("turtle")
turtle.width(2)
turtle.speed(0.5)

def draw_flower(increment):
    for i in range(int(360/increment)):
        turtle.pencolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))
        turtle.circle(150)
        turtle.right(increment)

draw_flower(5)

screen.exitonclick()