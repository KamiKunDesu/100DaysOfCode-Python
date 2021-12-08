'''This is going to be the ball class for the ball that moves back and forth across the screen'''
from turtle import Turtle

class Ball(Turtle):
    '''This is the ball class'''

    def __init__(self):
        '''This method sets the initial state of the ball'''
        
        # First inherit from the Turtle class
        super().__init__()
        #Then set up the ball
        self.initialise_ball()
        self.y_move = 8
        self.x_move = 6

    def initialise_ball(self):
        '''This function is going to make the ball the right parameters'''
        
        # Make it super fast so no move animation
        self.speed('fastest')
        # Take the pen up
        self.penup()
        # Make it a square
        self.shape('circle')
        # Make it white
        self.color('white')
        # Make sure it's in the right place
        self.goto(0,0)

    def move(self):
        '''This method will move the ball'''
        
        # Increment by the new X and Y coordinate
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def collide(self, x_or_y):
        '''This function handles collisions by reversing the direction of the movement in the x or y plane'''

        # If-Else to handle each plane
        if x_or_y == 'x':
            # Simply reverse the direction in the necessary plane and increase speed because paddle hit
            self.x_move *= -1
            self.increase_ball_speed()
        elif x_or_y == 'y':
            # Simply reverse the direction in the necessary plane
            self.y_move *= -1
            

    def increase_ball_speed(self):
        '''This method increases the ball speed on collision'''
        
        # Increase the movement variables in the 3:4 ratio
        # First account for orientation and then increase maintaining the ratio
        if self.y_move < 0:
            self.y_move -= 0.5
        else:
            self.y_move += 0.5
        if self.x_move < 0:
            self.x_move -= 0.3725
        else:
            self.x_move += 0.3725

    def reset(self):
        '''This method resets the ball if it goes out of bounds and starts it moving in the other players direction'''

        # Send it back to the center
        self.goto(0,0)
        # Reverse the X direction and reset speed
        self.x_move *= -1 * (6/self.x_move)
        self.y_move = 8
