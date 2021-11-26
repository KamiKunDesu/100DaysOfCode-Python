'''
This is one of the turtle challenges that I had to complete - I made some art with it, I call this: "The Alt Random Pipeline"
which is of course a play on the famous youtube alt right pipeline
'''
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


turtle = Turtle()
turtle.shape("turtle")
turtle.width(10)
turtle.speed(0.5)
for i in range(1000):
    turtle.pencolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))
    turtle.forward(20)
    turtle.right(90*random.choice([1,3,4]))


screen.exitonclick()