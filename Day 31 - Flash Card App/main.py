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
DATAFILE_TRAINED = "data/words_to_learn.csv"
SLEEP_TIMER = 3

from tkinter import *
import pandas
import random
import time

# Import data
try:
    df = pandas.read_csv(DATAFILE_TRAINED)
# Load initial file if no trained file is found or if all words have been learned
except (FileNotFoundError, pandas.errors.EmptyDataError) as e:
    df = pandas.read_csv(DATAFILE)

to_learn = df.to_dict(orient="records")
current_card = {}

# Flip to next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # Front of card
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text=LANGUAGE_B, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE_B], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    # Back of card
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text=LANGUAGE_A, fill="white")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE_A], fill="white")

def success_card():
    global current_card, to_learn
    try:
        to_learn.remove(current_card)
    except ValueError:
        pass
    df_trained = pandas.DataFrame(to_learn)
    df_trained.to_csv(DATAFILE_TRAINED, index=False)
    next_card()

def fail_card():
    next_card()

# UI Setup
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas_width = 800
canvas_height = 526
canvas = Canvas(width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(canvas_width/2, canvas_height/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(canvas_width/2, canvas_height/2 - 113, text=LANGUAGE_A, font=FONT_SMALL)
card_word = canvas.create_text(canvas_width/2, canvas_height/2, text="hi", font=FONT_LARGE)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=fail_card)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=success_card)
right_button.grid(row=1, column=1)

# Load first card
next_card()
window.mainloop()