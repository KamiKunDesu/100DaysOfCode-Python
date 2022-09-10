class Question:
    '''This is the question class which stores individual questions and answers and allows access
    to them in other classes'''

    def __init__(self, q_text, q_answer):
        '''This function initialises the Question class'''
        self.text = q_text
        self.answer = q_answer
