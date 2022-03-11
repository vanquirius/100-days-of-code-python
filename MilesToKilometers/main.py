# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 27 - Miles to Kilometers converter

import tkinter
from tkinter import *

def calculate_button_clicked():
    km_amount = round(1.689 * float(miles_entry.get()),5)
    km_amount_label.config(text=str(km_amount))

# Create window
window = tkinter.Tk()
window.title("Mile to Km Converter")
width = 300
height = 300
window.minsize(width, height)

# Add textbox input to convert
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

# Add fixed labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Add variable km label
km_amount_label = Label(text="0")
km_amount_label.grid(column=1, row=1)

# Add calculate button
calculate_button = Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(column=1, row=2)

# Keep window open until done
window.mainloop()