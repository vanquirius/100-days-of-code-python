# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-20

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 34 - Quizzler App

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUIZ_BG_COLOR = "white"
FONT_QUESTION = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.new_score = 0
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # flip_timer = window.after(3000, func=flip_card)

        # Canvas
        self.canvas_width = 300
        self.canvas_height = 250
        self.canvas = Canvas(width=self.canvas_width, height=self.canvas_height, bg=QUIZ_BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            self.canvas_width / 2,
            self.canvas_height / 2,
            width=self.canvas_width - 20,
            text="placeholder",
            font=FONT_QUESTION
        )

        # Label
        self.score_text = "Score: " + str(self.score)
        self.score_label = Label(text=self.score_text, fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Buttons
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.answer_true)
        self.right_button.grid(row=2, column=0)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.answer_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_question(self, input_answer):
        if self.quiz.still_has_questions():
            self.new_score = self.quiz.check_answer("True")
            if self.new_score > self.score:
                self.score = self.new_score
                self.give_feedback(True)
            else:
                self.give_feedback(False)
            self.score_text = "Score: " + str(self.score)
            self.score_label.config(text=self.score_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="No more questions!")
            self.right_button(state="disabled")
            self.wrong_button(state="disabled")

    def answer_true(self):
        self.answer_question("True")

    def answer_false(self):
        self.answer_question("False")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
