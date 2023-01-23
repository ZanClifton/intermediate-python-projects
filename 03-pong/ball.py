from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        self.setheading(45)
        self.forward(MOVE_DISTANCE)
