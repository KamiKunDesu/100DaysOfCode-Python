'''This is going to be the snake class which will control the snake'''
from turtle import Turtle
import time

class Snake:
    '''This is the snake class'''

    def __init__(self):
        '''This function will set the inital state of the snake'''
        
        # Set up a list to store all the snail pieces in it
        self.tail_pieces = []
        # Generate the snake
        self.generate_initial_snake()
        # Set the head of the snake
        self.head = self.tail_pieces[0]

    def generate_initial_snake(self):
        '''This function generates the initial snake'''

        # Create three tail pieces and add them to the tail pieces list
        for i in range(3):
            # Using globals so that we can create variable names algorithmically
            globals()[f"tail_piece{i+1}"] = Turtle()
            self.tail_pieces.append(globals()[f"tail_piece{i+1}"])

        # Set each tail piece up to be the right shape and colour and in the right position
        for counter, tail_piece in enumerate(self.tail_pieces):
            tail_piece.shape("square")
            tail_piece.color("white")
            tail_piece.penup()
            tail_piece.setposition(-20*counter, 0)

    def extend(self):
        '''This function adds a piece onto the snake'''
        tail_piece = Turtle()
        tail_piece.shape("square")
        tail_piece.color("white")
        tail_piece.penup()
        tail_piece.setposition(self.tail_pieces[-1].position())
        self.tail_pieces.append(tail_piece)

    def move(self):
        '''This function defines the movement of the snake'''

        # A for loop goes through ever section of the snake and then pushes it to the following sections position
        for i in range(len(self.tail_pieces)-1, 0, -1):
            new_x = self.tail_pieces[i-1].xcor()
            new_y = self.tail_pieces[i-1].ycor()
            self.tail_pieces[i].goto(new_x, new_y)
    
        # Then finally it pushes the front of the snake forward
        self.head.forward(20)

    def up(self):
        '''This sets the snake to move up'''
        
        # First we need to check if the snake is facing down because it can't turn back on itself
        if self.head.heading() == 270:
            pass
        # And if it isn't change it to North
        else:
            self.head.setheading(90)

    def down(self):
        '''This sets the snake to move down'''
        
        # First we need to check if the snake is facing up because it can't turn back on itself
        if self.head.heading() == 90:
            pass
        # And if it isn't change it to South
        else:
            self.head.setheading(270)

    def right(self):
        '''This sets the snake to move right'''
        
        # First we need to check if the snake is facing left because it can't turn back on itself
        if self.head.heading() == 180:
            pass
        # And if it isn't change it to East
        else:
            self.head.setheading(0)

    def left(self):
        '''This sets the snake to move left'''

        # First we need to check if the snake is facing right because it can't turn back on itself
        if self.head.heading() == 0:
            pass
        # And if it isn't change it to West
        else:
            self.head.setheading(180)

    