from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("title")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 266, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

no_pic = PhotoImage(file="images/wrong.png")
no = Button(image=no_pic, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
no.grid(column=0, row=1)

yes_pic = PhotoImage(file="images/right.png")
yes = Button(image=yes_pic, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
yes.grid(column=1, row=1, padx=50)


window.mainloop()