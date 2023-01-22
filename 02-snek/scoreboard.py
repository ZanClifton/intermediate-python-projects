from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
MOVE = False


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score: {self.score}", move=MOVE, align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown
        self.write("GAME OVER", move=MOVE, align=ALIGNMENT,
                   font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=MOVE, align=ALIGNMENT,
                   font=FONT)
