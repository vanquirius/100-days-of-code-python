# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 57 - Templating Jinja

BLOG_URL = "https://api.npoint.io/b48a954824422ec94216"  # this gets pruned periodically, populate from blog-data.txt

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import requests

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)


def get_blog_data():
    # Get blog data from bin
    response = requests.get(url=BLOG_URL)
    response.raise_for_status()
    data = response.json()
    print("Obtained blog data)")
    return data


@app.route('/')
def home():
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    return render_template("index.html", posts=blog_posts)


@app.route('/blog/<num>')
def read_post():
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
