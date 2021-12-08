'''This is the car class which will be used to generate random cars to go across the screen'''
from turtle import Turtle
import random

class Car(Turtle):
    '''This is the Car class which will extend the Turtle class'''

    def __init__(self):
        '''The init function which sets the initial state'''
        # Inherit from the Turtle class
        super().__init__()
        # First make it fastest
        self.speed('fastest')
        # Take the pen up
        self.penup()
        # Make it a square shape
        self.shape('square')
        # Set it to a random primary colour
        self.color(random.choice(['red','blue','green','yellow','pink','purple','grey','orange']))
        # Make it the right size and make it face the right way
        self.setheading(180)
        self.shapesize(1, 2, 0)
        self.turtlesize(1, 2, 0)
        # Set the position
        self.goto(420, random.randint(-240, 240))