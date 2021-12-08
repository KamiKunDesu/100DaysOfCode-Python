'''This is going to be the crosser class which will be the main player of the game'''
from turtle import Turtle

class Crosser(Turtle):
    '''This is the crosser class which is the asset controlled by the player'''

    def __init__(self):
        '''This is the init function which sets the initial state of the player'''
        # First inherit
        super().__init__()
        # First make it fastest
        self.speed('fastest')
        # Take the pen up
        self.penup()
        # Make it a turtle shape
        self.shape('turtle')
        # Make it white
        self.color('green')
        # Set it's position
        self.goto(0, -275)
        # Set the heading
        self.setheading(90)
        
    def up(self):
        '''This function moves the turtle up and the screen'''
        
        self.forward(10)

    def reset(self):
        '''This reset function sends the turtle back to it's original position'''
        
        self.goto(0,-275)

