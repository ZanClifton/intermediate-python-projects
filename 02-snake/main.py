from turtle import Screen, Turtle
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

screen.update()

snek = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snek.move()

screen.exitonclick()
