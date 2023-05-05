from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ------------------------- RETRIEVE WORDS ---------------------------- #

words = pandas.read_csv("data/french_words.csv")
words_dict = {row.French: row.English for (index, row) in words.iterrows()}
words_list = [row.French for (index, row) in words.iterrows()]

def select_word():
    selected_word = choice(words_list)
    translation = words_dict[selected_word]

    canvas.itemconfig(word, text=selected_word)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("title")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="word", font=WORD_FONT)

select_word()

# Buttons

no_pic = PhotoImage(file="images/wrong.png")
no = Button(image=no_pic, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=select_word)
no.grid(column=0, row=1)

yes_pic = PhotoImage(file="images/right.png")
yes = Button(image=yes_pic, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=select_word)
yes.grid(column=1, row=1, padx=50)


window.mainloop()