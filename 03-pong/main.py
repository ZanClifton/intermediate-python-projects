from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball

game_speed = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
