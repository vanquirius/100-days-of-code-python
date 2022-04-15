# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 57 - Templating Jinja

from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
import requests

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
BLOG_URL = "https://api.npoint.io/b48a954824422ec94216"  # this gets pruned periodically

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

year = datetime.now().year

def guess_age_gender(input_name):
    params = {
        "name": input_name
    }
    # Get age from API
    response_age = requests.get(url=AGIFY_URL, params=params)
    response_age.raise_for_status()
    data_age = response_age.json()
    age = data_age.get("age")

    # Get gender from API
    response_gender = requests.get(url=GENDERIZE_URL, params=params)
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    gender = data_gender.get("gender")

    return age, gender

def get_blog_data():
    # Get blog data from bin
    response = requests.get(url=BLOG_URL)
    response.raise_for_status()
    data = response.json()
    print("Obtained blog data)")
    return data

@app.route("/")
def homepage():
    return render_template("index.html", year=year, name="Marcelo")

# Guess age and gender dynamically from name in URL
@app.route("/guess/<name>")
def guess(name):
    age, gender = guess_age_gender(name)
    return render_template("guess.html", year=year, name=name, age=age, gender=gender)

# Guess age and gender dynamically from name in URL
@app.route("/blog")
def blog():
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    return render_template("blog.html", posts=blog_posts)

if __name__ == "__main__":
    app.run()
