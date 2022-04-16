# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-13

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 29 - MyPass - Password Manager

DEFAULT_EMAIL = "sample@email.com"

from tkinter import *
from tkinter import messagebox
import secrets
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Create a new random password
    password_entry.delete(0, END)
    str_size = 20
    new_password = secrets.token_urlsafe(str_size)
    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    # Save data on data.txt
    website = website_entry.get()
    email_username = emailusername_entry.get()
    password = password_entry.get()
    data_string = "\n" + str(website) + "," + str(email_username) + "," + str(password)

    # Check if website or password empty
    website_check = True
    password_check = True
    if website == "":
        messagebox.showerror(title="Error", message="Please enter a website")
        website_check = False
    if password == "":
        messagebox.showerror(title="Error", message="Please enter or generate a password")
        password_check = False

    if website_check and password_check:
        entry_ok = messagebox.askokcancel(title=website, message="Details entered:" + "\nWebsite: " + str(website) +"\nE-Mail/Username: " + str(email_username) + "\nPassword: " + str(password))

        if entry_ok:
            outputfile = "data.txt"
            with open(outputfile, mode="a") as f:
                f.write(data_string)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

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
emailusername_entry.insert(END, DEFAULT_EMAIL)
emailusername_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Add buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
