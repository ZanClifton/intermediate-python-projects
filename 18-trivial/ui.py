from tkinter import *

from quiz_brain import QuizBrain

BACKGROUND = "#375362"
YES = "#ABFF4F"
NO = "#F58FA5" # "#EE4266"
OFF_WHITE = "#D8DAE9" # "#BDC2DB" # "#B9C0DA"


class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivial")
        self.window.config(padx=20, pady=20, bg=BACKGROUND)

        self.score_label = Label(text="Score: 0", fg=OFF_WHITE, bg=BACKGROUND)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=OFF_WHITE)
        self.question = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Question text", 
            font=("Arial", 20, "italic"), 
            fill=BACKGROUND
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        true_pic = PhotoImage(file="images/right.png")
        self.true = Button(
            image=true_pic, 
            highlightthickness=0, 
            highlightcolor=BACKGROUND, 
            highlightbackground=BACKGROUND, 
            command=self.check_true_button
        )
        self.true.grid(column=0, row=2)
        
        false_pic = PhotoImage(file="images/wrong.png")
        self.false = Button(
            image=false_pic, 
            highlightthickness=0, 
            highlightcolor=BACKGROUND, 
            highlightbackground=BACKGROUND, 
            command=self.check_false_button
        )
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg=OFF_WHITE)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            if self.quiz.score <= len(self.quiz.question_list)/2:
                end_t = f"Bad luck! You scored {self.quiz.score}/{len(self.quiz.question_list)}"
            else:
                end_t = f"Congratulations! You scored {self.quiz.score}/{len(self.quiz.question_list)}"
            self.canvas.itemconfig(self.question, text=end_t)
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg=YES)
        else:
            self.canvas.configure(bg=NO)
        self.window.after(1000, self.get_next_question)