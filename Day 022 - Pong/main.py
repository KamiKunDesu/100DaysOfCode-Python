'''
Day 22 of 100 days of code python challenge - The purpose of todays project is to build the classic best selling game
pong using pythons built in GUI module, turtle 
'''
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from tkinter import messagebox
import time



def main():
    '''This is the main function, it will contain all the code so that this file will not run as an import
    and will only run as a script'''

    #Initialise the screen
    screen = Screen()
    #Set up the screen
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.bgcolor('black')
    screen.tracer(0)

    # Initialise the left and right paddles, the ball and the scoreboard
    right_paddle = Paddle(350, 0)
    left_paddle = Paddle(-350, 0)
    ball = Ball()
    scoreboard = Scoreboard()

    # Set up the event listeners
    screen.listen()
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")
    screen.onkeypress(main, 'c')

    #Turn the game on and keep running a tracer buffer so that it updates on each move
    game_on = True
    while game_on:
        # Update the screen on each buffer
        screen.update()
        time.sleep(0.05)

        # Get the ball moving
        ball.move()

        # Detect collision with wall and reverse direction
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.collide('y')
        # Detect collision with either paddle and reverse direction, turtle is a point in the center of the paddle
        # So check that the ball is within 50 pixels of the paddle (which coves the whole width from either side from the center)
        # But also check if that it is at the same time about to go past the paddle, i.e. the paddle stops it
        if (ball.distance(right_paddle) < 50 and ball.xcor() > 325) or (ball.distance(left_paddle) < 50 and ball.xcor() < -325):
            ball.collide('x')

        # Detect out of bounds on right side, increase score and reset - end game if winning score reached
        if ball.xcor() > 370:
            scoreboard.l_score_inc()
            if scoreboard.l_score == 15:
                winner = "left"
                game_on = False
            ball.reset()
        
        # Detect out of bounds on left side, increase score and reset - end game if winning score reached
        elif ball.xcor() < -370:
            scoreboard.r_score_inc()
            if scoreboard.r_score == 15:
                winner = "right"
                game_on = False
            ball.reset()

    screen.update()
    messagebox.showinfo(title="Winner", message=f'The {winner} side player won!\nPress c to play again')
    
    def reset():
        '''This function should reset the game'''
        screen.clear()
        main()

    screen.onkey(reset, "c")
    


# Make it so the program runs if isn't being imported
if __name__ == "__main__":
    main()