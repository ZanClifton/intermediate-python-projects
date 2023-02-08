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
states_list = data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:

    guess = screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a US State: ").title()

    if guess == "Exit":
        missed_states_list = [
            state for state in states_list if state not in correct_guesses]

        missed_states = {"missed states": missed_states_list}
        data_frame = pandas.DataFrame(missed_states)
        data_frame.to_csv("./revision/states_to_learn.csv")
        break

    for index in states_dict["state"]:
        if guess == states_dict["state"][index]:
            xpos = states_dict["x"][index]
            ypos = states_dict["y"][index]
            pen.write_state(guess, xpos, ypos)
            correct_guesses.append(guess)
