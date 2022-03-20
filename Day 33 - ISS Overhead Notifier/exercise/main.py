# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-19

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 33 - ISS Over Head Notifier - exercise

from tkinter import *
import requests

def get_quote():
    # Get random Kanye quote from Kanye API site
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    try:
        canvas.itemconfig(quote_text, text=quote)
    except NameError:
        pass
    return quote

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()