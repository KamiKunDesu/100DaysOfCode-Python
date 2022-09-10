import html

class QuizBrain:
    '''This is the QuizBrain class which brings in questions and handles the underlying game.
    It keeps track of the score as well as handling the Questions (from the Question class) and
    serving up new Questions'''

    def __init__(self, q_list):
        '''Initialises QuizBrain class'''

        # Set the question number
        self.question_number = 0
        # Set the score
        self.score = 0
        #Bring the questions in from the list of questions
        self.question_list = q_list
        # Set the current question
        self.current_question = None

    def still_has_questions(self):
        '''This function checks if there are any questions left'''

        # Check if question number is less than the number of questions in the question list (it should always be one less)
        # and then if this isn't the case there are no questions left
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''This function calls the next question, and also returns some text with the number of
        the question and the question itself'''

        # This makes the current question the next question in the list
        self.current_question = self.question_list[self.question_number]
        # Add 1 on to the question number for when the next question gets called
        self.question_number += 1
        # Since the questions are pulled down from an API they have html escapes in them
        # so get rid of those escapes
        q_text = html.unescape(self.current_question.text)
        # Finally return a string which can be shown in the UI showing the question number and the question
        return f"Q.{self.question_number}: {q_text} (True/False): "


    def check_answer(self, user_answer):
        '''This method checks whether the user answer is correct or not'''

        # Store the correct answer in a correct answer variable
        correct_answer = self.current_question.answer
        # Check that the user answer is the same as the correct answer (normailising the text with the normal() method)
        if user_answer.lower() == correct_answer.lower():
            # If it is then increase the score and return True
            self.score += 1
            return True
        else:
            # Otherwise return False
            return False