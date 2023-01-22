from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import ScoreBoard

game_speed = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

screen.update()

snek = Snake()
food = Food()
sb = ScoreBoard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(game_speed)

    snek.move()

    if snek.head.distance(food) < 15:
        food.refresh()
        snek.extend()
        sb.update_score()

    if snek.head.xcor() > 280 or snek.head.xcor() < -300 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        game_is_on = False
        sb.game_over()

    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            game_is_on = False
            sb.game_over()

screen.exitonclick()
