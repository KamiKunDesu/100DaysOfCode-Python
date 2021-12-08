'''This is going to be the paddle class which describes both paddle objects'''
from turtle import Turtle

class Paddle(Turtle):
    '''The paddle class which the players use to hit the ball back and forth'''

    def __init__(self, x_pos: int, y_pos: int):
        '''This is the init function which sets the initial state of the paddle'''
        #Initialise a turtle that looks like our paddle
        super().__init__()
        self.initialise_self(x_pos, y_pos)
        
    def initialise_self(self, x_pos: int, y_pos: int) -> Turtle:
        '''This function is just going to set the turtle element of the paddle up'''

        # Make it super fast so no move animation
        self.speed('fastest')
        # Take the pen up
        self.penup()
        # Make it a square
        self.shape('square')
        # Make it white
        self.color('white')
        # Make it the right size
        self.shapesize(5, 1, 0)
        self.turtlesize(5, 1, 0)
        # Set it's position
        self.goto(x_pos, y_pos)

    def up(self):
        '''This function will move the paddle up'''
        
        # Adjust y_cor up by 20 if not at boundary
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        '''This function will move the paddle down'''
        
        # Adjust y_cor down by 20 if not at boundary
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
