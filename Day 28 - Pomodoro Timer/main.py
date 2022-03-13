# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 28 - Pomodoro Timer

from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

iterations = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    global iterations
    iterations = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global iterations
    iterations += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if iterations == 9:
        iterations = 1
    print("Iteration: " + str(iterations))
    if iterations in (1, 3, 5, 7):
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN)
    if iterations in (2, 4, 6):
        count_down(short_break_sec)
        timer_label.config(text="Short break", fg=PINK)
    if iterations == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def convert(seconds):
   seconds = seconds % (24 * 3600)
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60
   try:
       return "%02d:%02d" % (minutes, seconds)
   except:
       return "00:00"

def count_down(count):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        count_mmss = convert(count)
        canvas.itemconfig(timer_text, text=count_mmss)
    if count == 0:
        start_timer()
        mark = ""
        work_sessions = math.floor(iterations/2)
        for i in range(work_sessions):
            mark += "✔"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


# Window setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_iter = 1

# Tomato setup
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add fixed labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Add buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Add variable tick
tick_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
tick_label.grid(column=1, row=2)

window.mainloop()
