from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_speed = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
sb = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)

    sb.update_scoreboard()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 380:
        ball.reset_position()
        sb.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        sb.r_point()


screen.exitonclick()
