from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ---------------------------- NEXT CARD ------------------------------- #

words = pandas.read_csv("data/french_words.csv")
words_to_learn = words.to_dict(orient="records")


def next_card():
    global flip_timer, translation
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    selected_word = choice(words_to_learn)
    translation = selected_word["English"]

    canvas.itemconfig(word, text=selected_word["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")

    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARDS ------------------------------ #


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word, text=translation, fill="white")

    canvas.itemconfig(language, text="English", fill="white")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("title")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="word", font=WORD_FONT)

flip_timer = window.after(3000, flip_card)


# Buttons

no_pic = PhotoImage(file="images/wrong.png")
no = Button(
    image=no_pic,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
no.grid(column=0, row=1)

yes_pic = PhotoImage(file="images/right.png")
yes = Button(
    image=yes_pic,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
yes.grid(column=1, row=1, padx=50)

next_card()

window.mainloop()
