from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_pic)
canvas.create_text(100, 135, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

header = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
header.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

count_display = Label(text=" ✔️✔️✔️✔️",
                      bg=YELLOW, font=(FONT_NAME, 20))
count_display.grid(column=1, row=3)

window.mainloop()
