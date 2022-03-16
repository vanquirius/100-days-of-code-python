# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-15

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 31 - Flash Card App

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_A = "English"
LANGUAGE_B = "French"
FONT_SMALL = ("Arial", 40, "italic")
FONT_LARGE = ("Arial", 60, "bold")
DATAFILE = "data/french_words.csv"

from tkinter import *
import pandas
import random

# Import data
def import_flashcard_data():
    df = pandas.read_csv(DATAFILE)
    to_learn = df.to_dict(orient="records")
    print(to_learn)

# Select random words
#def select_random_words(df, rows):
#    random_selection = random.randint(0, rows)
#    language_a_word = df.iat[random_selection,1]
#    language_b_word = df.iat[random_selection,0]
#    return language_a_word, language_b_word

def next_card():
    current_card = random.choice(to_learn)
    print(current_card["French"])

# Runtime
to_learn = import_flashcard_data()
#language_a_word, language_b_word = select_random_words(df, rows)

# UI Setup

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas_width = 800
canvas_height = 526
canvas = Canvas(width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(canvas_width/2, canvas_height/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(canvas_width/2, canvas_height/2 - 113, text=LANGUAGE_A, font=FONT_SMALL)
canvas.create_text(canvas_width/2, canvas_height/2, text="hi", font=FONT_LARGE)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

window.mainloop()