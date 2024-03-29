from turtle import Turtle 
from random import choice, randint

COLORS = ["red", "orange", "black", "deep pink",
          "maroon", "green", "blue", "purple", "midnight blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.goto(300, randint(-10, 10) * 20.5)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
