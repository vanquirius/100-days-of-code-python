# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 55 - Guess the Number

from flask import Flask
from flask_wtf.csrf import CSRFProtect
import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route("/")
def homepage():
    with open("index.html", mode="r") as f:
        html_content = f.read()
        return html_content

@app.route("/<int:number>")
def number(number):
    if number == random_number:
        with open("right.html", mode="r") as f:
            html_content = f.read()
            return html_content
    elif number > random_number:
        with open("too_high.html", mode="r") as f:
            html_content = f.read()
            return html_content
    else:
        with open("too_low.html", mode="r") as f:
            html_content = f.read()
            return html_content

if __name__ == "__main__":
    app.run()