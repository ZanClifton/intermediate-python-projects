import re

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)

question_bank = []

for question in question_data:
    question_text = question["question"].replace("&#039;", "'")
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_result()