'''Day 25 of 100 days of code python challenge - The purpose of todays project is to make a program which acts like the
American States Quiz game on sporcle in which you try to guess all the American states on a map. It will demonstrate
an understanding of the pandas library as well as csv files and also help develop the use of the turtles library
'''
import turtle
import pandas as pd
import time

def main():
    '''Put everything inside a main function so that we can choose only to run it if the file is accessed
    as a script'''
    
    # Initialise a screen
    screen = turtle.Screen()
    # Change the title of the game
    screen.title("U.S. States Game")
    # Store the map image in a variable
    image = "blank_states_img.gif"
    # Use that variable to add a new shape to turtle
    screen.addshape(image)
    # Change the shape of the turtle to the image of the map
    turtle.shape(image)
    # Start tracking how many states have been correctly guessed
    states_guessed = 0
    # Read in our csv data into a pandas dataframe
    data = pd.read_csv("50_states.csv")
    # Make a new turtle called pen to write
    pen = turtle.Turtle()
    # bring the pen up
    pen.penup()
    pen.speed("fastest")
    pen.hideturtle()
    # Initialise a list of the states guessed to keep track so that at the end we can make a csv of all the
    # state that were missed at game end
    states_guessed_list = []

    # Make a function to write the data in the specific place
    def write_name(name):
        '''This function takes a name parameter and writes the name of the state on the correct place in the map'''
        # Get the coords from the dataframe
        x_cor = int(data[data.state == name].x)
        y_cor = int(data[data.state == name].y)
        # Go to coords and write the state name
        pen.goto(x_cor, y_cor)
        pen.write(name, align="center", font=["Arial", 8, "normal"])

    # Set a loop for the game
    while states_guessed < 50:
         # Get an answer from the user
        answer_state = screen.textinput(title=f"{states_guessed}/50 States Correct", prompt="What's another states name?")
        # Convert it to the right case which is title case
        answer_state = answer_state.title()
        # End game if we chose exit
        if answer_state == "Exit":
            break
        # Check if the state is correct and then write it to the correct place and increase the amount of states guessed by 1
        if answer_state in data["state"].tolist() and not answer_state in states_guessed_list:
            write_name(answer_state)
            states_guessed += 1
            states_guessed_list.append(answer_state)

    # Print congratulations message

    # Make a dictionary to be turned into a csv of all the states that were missed to be learned for later
    states_to_learn_dict = {
        "States To Learn": [state for state in data["state"].tolist() if state not in states_guessed_list]
    }
    # Make them into a data frame
    states_to_learn_df = pd.DataFrame(states_to_learn_dict)
    # Make them into a csv
    states_to_learn_df.to_csv("states_to_learn.csv", index=False)
 
if __name__ == "__main__":
    main()