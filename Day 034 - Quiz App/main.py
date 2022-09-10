'''Day 034 - The purpose of this project is to learn more about APIs and fuse it with my understanding of
classes and object oriented programming, as well as my knowledge of GUIs, specifically Tkinter. The program
is an quiz game that re uses code from day 017, however it makes an API call to the place where the original
question data came from. It is also now in a UI which is handled by a class'''
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initialise a list for the question bank questions
question_bank = []
# For loop to bring all the questions into the list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Make the quiz using the QuizBrain class
quiz = QuizBrain(question_bank)

# Make the GUI using the QuizInterface class, this will also run the interface because the class itself
# Calls the Tkinter mainloop method
quiz_interface = QuizInterface(quiz)
