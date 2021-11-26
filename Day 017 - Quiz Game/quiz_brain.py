'''This class is the quiz brain class which manages asking the questions to the user
as well as keeping track of the score and question count'''
import re
import time
import sys

class QuestionBrain:
    '''This is the quiz brain class which handles the actual quiz game'''

    def __init__(self, question_list: list):
        '''This is the initialize function'''
        
        # Give the initial attributes of the class
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        '''This method checks if there are still questions left to be answered or not'''
        # Simple boolean return statement to check that the number of questions asked is less than that
        # in the question bank
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''This method gets a question from the bank and asks the user for their answer'''
        
        # Pull the current question from the question bank
        current_question = self.question_list[self.question_number]
        # Increase question number by one
        self.question_number += 1

        # Start a while loop with break flags to ensure the user gives a valid answer
        input_flag = False
        counter = 10
        while counter and not input_flag:
            # Get the user input
            user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            time.sleep(1)
            # Check if it's a valid input using regex
            if re.compile("[Tt][Rr][Uu][Ee]").fullmatch(user_input) or re.compile("[Tt]").fullmatch(user_input):
                # Format it correctly for later matching
                user_input = "True"
                input_flag = True
            elif re.compile("[Ff][Aa][Ll][Ss][Ee]").fullmatch(user_input) or re.compile("[Ff]").fullmatch(user_input):
                # Format it correctly for later matching
                user_input = "False"
                input_flag = True
            else:
                counter -= 1
                if not counter:
                    print("Too many invalid inputs, the program will now exit")
                    time.sleep(4)
                    sys.exit()
                print("Please give a valid input 'True' or 'False'")
                time.sleep(1)
        
        self.check_answer(current_question, user_input)

    def check_answer(self, question, user_input):
        '''This function checks if the answer is correct, then increases the user score
        or doesn't and prints the current result'''

        if question.answer == user_input:
            print(f"That's correct, the answer was {question.answer}")
            time.sleep(1)
            self.score += 1
        else:
            print(f"That's not correct, the answer was {question.answer}")
            time.sleep(1)
        
        print(f"Your current score is {self.score}/{self.question_number}")
        time.sleep(1)

                