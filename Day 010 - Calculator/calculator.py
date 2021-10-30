'''
Practicing making and using classes in my projects
'''
import sys
import time

# Making a calculator class
class Calculator():
    
    def calculate_first_input(self):
        '''This function gets the first number, operator, and second number'''

        first_num = self.get_first_number()
        operation = self.get_operation()
        next_num = self.get_next_number()
        computed_num = self.compute_sum(first_num, next_num, operation)
        print(f'{first_num} {operation} {next_num} = {computed_num}')
        return computed_num

    def calculate_subsequent_input(self, first_num: float) -> float:
        '''This function calculates all subsequent operations'''

        operation = self.get_operation()
        next_num = self.get_next_number()
        computed_num = self.compute_sum(first_num, next_num, operation)
        print(f'{first_num} {operation} {next_num} = {computed_num}')
        return computed_num

    def get_first_number(self) -> float:
        '''This function gets the first float that is used in the calculation'''
        
        # set up a counter and while block to get a valid input
        counter = 10
        while counter:  
            try:
                first_number = float(input("What's the first number?: "))
                counter = 0
                continue
            except ValueError:
                counter -= 1
                if not counter:
                    print("Too many wrong inputs, program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please give a valid number")
        return first_number

    def get_next_number(self) -> float:
        '''This function gets the second float that is used in the calculation'''
        
        # set up a counter and while block to get a valid input
        counter = 10
        while counter:  
            try:
                next_number = float(input("What's the next number?: "))
                counter = 0
                continue
            except ValueError:
                counter -= 1
                if not counter:
                    print("Too many wrong inputs, program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please give a valid number")
        return next_number

    def get_operation(self) -> str:
        '''This function takes in a user input and returns the correct operation'''

        # set up a counter and while block to get a valid input
        counter = 10
        while counter:  
            operation = input("Please pick an operation from (+ - / *): ")
            if operation not in ['+', '-', '/', '*']:
                counter -= 1
                if not counter:
                    print("Too many wrong inputs, program will now exit")
                    time.sleep(3)
                    sys.exit()
                print("Please give a valid operation from [+, -, /, *]")
            else:
                counter = 0
                continue
        return operation

    def compute_sum(self, num_a: float, num_b: float, operation: str) -> float:
        '''This function computes the sum of the operation and returns the result'''

        if operation == '+':
            return num_a + num_b

        elif operation == '-':
            return num_a - num_b
        
        elif operation == '/':
            return num_a / num_b

        elif operation == '*':
            return num_a * num_b