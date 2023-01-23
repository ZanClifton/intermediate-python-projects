from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)
