# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-17

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 60 - POST Request Flask HTML Forms

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "supersecretkey123456789"
csrf = CSRFProtect(app)
csrf.init_app(app)


@app.route('/')
def home():
    # Homepage for blog
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_login_data():
    # Process received data
    username = request.form['username']
    password = request.form['password']
    html = "<h1> Name: " + str(username) + ", Password: " + str(password)
    return html


if __name__ == "__main__":
    app.run(debug=True)
