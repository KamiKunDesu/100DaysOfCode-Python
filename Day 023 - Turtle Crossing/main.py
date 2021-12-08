'''Day 23 of 100 days of code python challenge - The purpose of todays project is to build the game Turtle crosser, which is kind
of like the game crossy roads
'''
from turtle import Turtle, Screen
from crosser import Crosser
from car_manager import CarManager
import time
from scoreboard import Scoreboard


def main():
    '''This is the main function which will only call if the program is being run as a script and not
    as an import'''

    # Initialise the screen
    screen = Screen()
    # Set up the screen
    screen.setup(width=800, height=600)
    screen.title("Turtle Crosser")
    screen.bgcolor('white')
    screen.tracer(0)

    # Initialise the crosser, car manager, create a car and initialise scoreboard
    player = Crosser()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    car_manager.create_car()

    # Initialise event listeners
    screen.listen()
    screen.onkeypress(player.up, 'Up')

    # Turn the game on
    game_on = True
    # In a while loop so the screen keeps refreshing
    while game_on:
        # Update the screen then pause for a moment so that the assets don't appear to have infinite speed
        screen.update()
        time.sleep(0.05)

        # Every 6 cycles make a new car, reset the cycle counter and get rid of any off screen cars, should scale for move speed
        for i in range(int(car_manager.move_speed // 5)):
            car_manager.create_car()
            car_manager.update_list()

        # Move all the cars per once per frame            
        car_manager.move()

        # Detect collision with car
        for car in car_manager.cars:
            if player.distance(car) < 20:
                game_on = False
                scoreboard.game_over()

        # Detect if player reaches finish line
        if player.ycor() > 275:
            player.reset()
            car_manager.move_speed *= 1.2
            scoreboard.increase_score()

    def reset():
        '''This function should reset the game'''
        screen.clear()
        main()

    screen.onkey(reset, "c")

    screen.exitonclick()




# Make it run when called as a script
if __name__ == "__main__":
    main()