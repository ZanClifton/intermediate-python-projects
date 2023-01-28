from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# starts at the bottom of the screen
# moves up only - cannot move left, right or back


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown", "dark olive green")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
