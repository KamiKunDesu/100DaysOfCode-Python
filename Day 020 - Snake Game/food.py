'''This is going to be the class that is the food class for the snake to eat'''
from turtle import Turtle
import random

class Food(Turtle):
    '''This is the food class'''

    def __init__(self):
        '''This is the initialization method'''

        # Inherit from the Turtle class first
        super().__init__()
        # Then set up the foods shape and colour etc.
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")

        # Generate a random coordinate to appear on
        self.randomx = random.randrange(-280,280,20)
        self.randomy = random.randrange(-280,260,20)

        # Send it to the random position
        self.goto(self.randomx, self.randomy)

    def refresh(self):
        '''This method refreshes the location of the food every time the snake eats a piece of food'''

        # Generate a random coordinate to appear on
        self.randomx = random.randrange(-280,280,20)
        self.randomy = random.randrange(-280,260,20)

        # Send it to the random position
        self.goto(self.randomx, self.randomy)