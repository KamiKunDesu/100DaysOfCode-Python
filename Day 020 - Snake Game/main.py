'''
Day 20 of 100 days of code python challenge - The purpose of todays project is to build the classic snake game from 
times past - this project will also span across Day 21 
'''
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Make it all inside a main function to stop it launching on import
def main():
    # Set up the screen for the game
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # Generate the snake
    snake = Snake()

    # Generate the scoreboard
    scoreboard = Scoreboard()

    # Set up the event listeners
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # Generate first random food
    food = Food()

    # Turn the game on
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 10:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 266 or snake.head.ycor() < -290:
            scoreboard.game_over()
            game_on = False

        # Detect collision with tail
        for tail_piece in snake.tail_pieces[1:]:
                if snake.head.distance(tail_piece) < 10:
                    scoreboard.game_over()
                    game_on = False

    screen.exitonclick()

if __name__ == "__main__":
    main()