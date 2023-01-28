import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = []

for i in range(1):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(player.move, "Up")

count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    count += 1

    if count % 8 == 0:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move()
        if player.distance(car) < 15:
            game_is_on = False

screen.exitonclick()
