'''This is going to be the scoreboard class which keeps track of the score'''
from turtle import Turtle

class Scoreboard(Turtle):
    '''This is the scoreboard class which keeps control of the scoreboard'''

    def __init__(self):
        '''This is the initialization function'''
        # First inherit from the Turtle class
        super().__init__()
        # Then set up a score to keep track 
        self.score = 0
        # Set the position
        self.setposition(0, 266)
        # Hide the Turtle
        self.hideturtle()
        # Make colour of the score title white
        self.color("white")
        # Then write it to the top of the board
        self.write(f"Score: {self.score}", False, align="center", font=("Courier",24,'normal'))

    def increase_score(self):
        '''This method increases the score whenever a the snake gets food'''
        
        # Increment the score
        self.score += 1
        # Rewrite
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Courier",24,'normal'))

    def game_over(self):
        '''This function makes the title read game over'''

        # Write game over in the centre of the screen
        self.goto(0,0)
        self.write("Game Over!", False, align="center", font=("Courier",24,'normal'))
        self.goto(0,-24)
        self.write("Press c To Play Again", False, align="center", font=("Courier",24,'normal'))