'''
This is one of the turtle challenges that I learned - I made some art with it, I call this: "Smoothing out rough edges"
'''
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.setx(-50)
turtle.sety(200)
turtle.pendown()
for i in range(3,50):
    turtle.pencolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))
    for j in range(i):
        turtle.forward(50)
        turtle.right((360/i))


screen.exitonclick()