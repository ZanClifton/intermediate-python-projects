import turtle
import pandas
from pen import Pen

screen = turtle.Screen()
screen.title("US States Game")
image = "./resources/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = Pen()
pen.color("black")
pen.hideturtle()
pen.penup()

data = pandas.read_csv("./resources/states.csv")

states_dict = data.to_dict()
# print(states_dict["state"])

correct_guesses = 0

game_is_on = True

while game_is_on:
    if correct_guesses == 50:
        game_is_on = False
        pen.win()
        break

    guess = screen.textinput(
        title=f"{correct_guesses}/50 States Correct", prompt="Name a US State: ").title()

    for index in states_dict["state"]:
        if guess == states_dict["state"][index]:
            correct_guesses += 1
            xpos = states_dict["x"][index]
            ypos = states_dict["y"][index]
            pen.write_state(guess, xpos, ypos)

screen.exitonclick()
