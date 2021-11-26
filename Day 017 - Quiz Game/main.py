'''
Day 17 of 100 days of code python challenge - The purpose of this project is to make a quiz game using classes
to demonstrate an understanding of object oriented programming. It asks the users true or false questions
and keeps track of their score when they make guesses
'''
from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain
import time

# Initialise the question bank ready for
question_bank = []

# Import all the questions the question bank and initialise them as a question class
for question_datum in question_data:
    question = Question(question_datum["text"], question_datum["answer"])
    question_bank.append(question)

# Initialise a QuizBrain with the question bank
quiz_brain = QuestionBrain(question_bank)

# Initialise a while loop to keep asking questions until there's none left
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

# Print final score
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
time.sleep(1)
print("Thanks for playing!")


