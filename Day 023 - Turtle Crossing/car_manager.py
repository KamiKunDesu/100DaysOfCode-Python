'''This is going to be the car manager class which handles the cars'''
from car import Car
import random
import math

class CarManager:
    '''This is the car manager class'''

    def __init__(self):
        '''Sets the initial state of the manaager'''
        # Give it a movement speed for the cars
        self.move_speed = 5
        # Give it a list to store cars in
        self.cars = []

    def create_car(self):
        '''This method creates a car'''
        number = random.randint(1,6)

        if number == 6:
        # Make a new car and append it to the list of cars
            self.cars.append(Car())

    def move(self):
        '''This method loops through each of the cars being managed and moves them across the screen'''

        for car in self.cars:
            car.forward(self.move_speed)

    def update_list(self):
        '''This function makes sure to remove any redundant cars from the list to avoid too many items stacking up'''

        for car in self.cars:
            if car.xcor() < -420:
                self.cars.remove(car)
        