'''This will be the scoreboard class which draws the scores of the game and other features'''
from turtle import Turtle

class Scoreboard(Turtle):
    '''This class is the scoreboard class'''

    def __init__(self):
        '''Sets the initial state of the scoreboard'''

        # First inherit from the turtle class
        super().__init__()
         # Make it white
        self.color('white')
        # Bring the pen up
        self.penup()
        # Hide the turtle because we just want it to draw not be seen
        self.hideturtle()
        # Add score attributes
        self.l_score = 0
        self.r_score = 0
        # Write scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        '''This function updates the scoreboard'''
    
        # Send to the left position and write left score
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        # Do the same for the right position
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_score_inc(self):
        '''increase left side score by 1'''

        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score_inc(self):
        '''increase right side score by 1'''

        self.r_score += 1
        self.clear()
        self.update_scoreboard()