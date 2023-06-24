from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOUR = "#375362"

class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivial")
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOUR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Question text", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOUR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_pic = PhotoImage(file="images/right.png")
        false_pic = PhotoImage(file="images/wrong.png")

        self.true = Button(image=true_pic, highlightthickness=0, highlightcolor=THEME_COLOUR, highlightbackground=THEME_COLOUR)
        self.true.grid(column=0, row=2)
        self.false = Button(image=false_pic, highlightthickness=0, highlightcolor=THEME_COLOUR, highlightbackground=THEME_COLOUR)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)