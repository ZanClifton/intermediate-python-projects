from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
SECONDS = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    count_display.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        header.config(text="Rest", fg=RED)
        countdown(LONG_BREAK_MIN * SECONDS)
    elif reps % 2 == 0:
        header.config(text="Rest", fg=PINK)
        countdown(SHORT_BREAK_MIN * SECONDS)
    else:
        header.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * SECONDS)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks = " "
        for number in range(work_sessions):
            marks += "✔️"
        count_display.config(text=marks)


        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_pic)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


header = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
header.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

count_display = Label(bg=YELLOW, font=(FONT_NAME, 20))
count_display.grid(column=1, row=3)

window.mainloop()
