import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cm = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    count += 1

    if count % 8 == 0:
        cm.create_car()

    cm.move()

    for car in cm.cars:
        if player.distance(car) < 15:
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        cm.speed_up()
        sb.level_up()

screen.exitonclick()
