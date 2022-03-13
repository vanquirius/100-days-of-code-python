# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-13

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 29 - MyPass - Password Manager

from tkinter import *
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    str_size = 20
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    new_password = ''.join(random.choice(allowed_chars) for i in range(str_size))
    password_entry.insert(END, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    pass

# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("MyPass - Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Add fixed labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
emailusername_label = Label(text="E-Mail/Username:")
emailusername_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Add entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
emailusername_entry = Entry(width=35)
emailusername_entry.insert(END, "sample@email.com")
emailusername_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Add buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
