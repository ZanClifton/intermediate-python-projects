from turtle import Turtle

FONT = ("Courier", 6, "normal")


class Pen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.pendown()
        self.write(f"{state}", FONT)
        self.penup()

    def win(self):
        self.goto(-360, 250)
        self.pendown()
        self.write("Congratulations! You did it!",
                   font=("Courier", 22, "normal"))
