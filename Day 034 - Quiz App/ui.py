from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    '''This class handles the user interface of the program which is built using Tkinter.'''

    def __init__(self, quiz_brain: QuizBrain):
        '''This is the init method which sets up the window for the game. It takes a Quizbrain
        as one of its arguments to handle all the underlying game logic which is displayed
        onto the UI'''

        # Initialise the quiz_brain
        self.quiz = quiz_brain
        # Create the window
        self.window = Tk()
        # Set the title
        self.window.title("Quizzler")
        # Set the background theme
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Add the score label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        # Put the score label onto the window
        self.score_label.grid(row=0, column=1)
        # Make a textbox to hold the question which has a white background and no border
        self.text_box = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # This adds the question text onto the text box
        self.question_text = self.text_box.create_text(
            150, # Sets the X parameter of the text
            125, # Sets the Y parameter of the text
            width=280, # Sets the width that the text can span
            text="Some Question Text", # Just a placeholder
            fill=THEME_COLOR, # Fill of the text box surrounding the text
            font=("Arial", 20, "italic")) # Set the font details
        # Place the text box onto the canvas
        self.text_box.grid(row=1, column=0, columnspan=2, pady=50)

        # Bring the image for the True button in from the local files
        true_image = PhotoImage(file="images/true.png")
        # Make the True button, give it the command for when it's clicked
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.on_true_click)
        # Put it on to the main window
        self.true_button.grid(row=2, column=0)

        # Exact same here but for the false button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.on_false_click)
        self.false_button.grid(row=2, column=1)

        # Call the method to get the next question which will use the QuizBrain to replace the default
        # text on the screen with the first Question in the question list of the QuizBrain
        self.get_next_question()
        # Finally run mainloop to launch the UI
        self.window.mainloop()

    def get_next_question(self):
        '''This function gets the next question from the QuizBrain and displays it onto the UI.
        It also handles the button state to prevent bugs that occur by clicking the button really
        fast, as well as disabling the buttons when there are no more questions left and displaying
        a final message'''

        # Set the text_box background to white, this line is to counter the effects of setting it to green
        # or red on wrong or right answer
        self.text_box.config(bg="white")
        # Reactivate True and False button, because we deactivate them when they're pressed to avoid bugs
        self.false_button.config(state="normal")
        self.true_button.config(state="normal")#
        # This checks if there are any questions left, and if there are it gets the next question, if there
        # aren't then it displays message and disables the true and false buttons
        if self.quiz.still_has_questions():
            # Get the next question from the QuizBrain
            q_text = self.quiz.next_question()
            # and display it on the UI
            self.text_box.itemconfig(self.question_text, text=q_text)
        else:
            # Display the final message when there's no more questions left
            self.text_box.itemconfig(self.question_text, text=f"You've reached the end of the quiz, your final score was {self.quiz.score}/10")
            # Disable all the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def on_true_click(self):
        '''This handles what happens when you press the True button'''

        # Store the correctness of the answer
        answer_correct = self.quiz.check_answer("True")
        # Update the score regardless
        self.score_label["text"] = f"Score {self.quiz.score}"
        if answer_correct:
            # If answer correct then briefly flash the screen green
            self.text_box.config(bg="green")
        else:
            # Otherwise flash it red
            self.text_box.config(bg="red")
        # Immediately disable both the true and false button to stop multi click bug
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        # Then after a short time call to the next question
        self.window.after(500, self.get_next_question)

    def on_false_click(self):
        '''This handles what happens when you press the False button'''

        # Uses the exact same logic as above - could probably be refactored to use a single method and
        # then have these other methods just call that method with an argument but its 10:25pm and
        # I'm just way to lazy to rewrite that at this time - especially after commenting up all my
        # code now. Seriously, if you're reading this - welcome. Consider this an Easter Egg.
        # Thank you for reading through my code. It means a lot. And to read in this detail is really
        # nice of you. Anyway, hope you like the code. Please send any cool update ideas you have to
        # my email at chessmasterkami1@gmail.com
        answer_correct = self.quiz.check_answer("False")
        self.score_label["text"] = f"Score {self.quiz.score}"
        if answer_correct:
            self.text_box.config(bg="green")
        else:
            self.text_box.config(bg="red")
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        self.window.after(500, self.get_next_question)
        

