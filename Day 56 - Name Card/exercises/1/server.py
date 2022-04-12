# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 56 - Name Card

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("angela.html")

if __name__ == "__main__":
    app.run()