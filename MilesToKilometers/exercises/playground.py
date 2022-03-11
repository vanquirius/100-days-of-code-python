# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 27
import tkinter
from tkinter import *

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return sum

add(1,2,3)

# Create window
window = tkinter.Tk()
window.title("My First GUI Program")
width = 500
height = 300
window.minsize(width, height)

# Button
def button_clicked():
    print("I got clicked")
    #my_label["text"] = "I got clicked"
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)
button2 = Button(text="Button #2")
button2.grid(column=1, row=1)

# Label
my_font = ("Arial", 24, "bold")
my_text = "I Am a Label"
my_label = tkinter.Label(text=my_text, font=my_font)
my_label.grid(column=0, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)

# Keep window open until done
window.mainloop()