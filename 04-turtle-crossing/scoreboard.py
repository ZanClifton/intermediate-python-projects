from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.pendown()
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown
        self.write("GAME OVER", font=FONT)
