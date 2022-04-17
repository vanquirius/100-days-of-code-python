# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-17

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 60 - POST Request Flask HTML Forms

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import requests
import os
from send_email import SendEmail

BLOG_URL = "https://api.npoint.io/46b7d5447ebd3c655f57"  # this gets pruned periodically, populate from blog-data.txt

app = Flask(__name__)
app.secret_key = "supersecretkey123456789"
csrf = CSRFProtect(app)
csrf.init_app(app)

# Set as 1 to choose SendGrid over SMTP
sendgrid_enabled = 1

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP

# Credentials
from_email = os.getenv("from_email")
sendGridToken = os.getenv("sendGridToken")  # If using SendGrid
email_password = os.getenv("email_password")  # If using SMTP
to_email = from_email  # Send e-mail to yourself

sendemail = SendEmail(from_email, smtp_server, smtp_port, email_password, sendGridToken)


def get_blog_data():
    # Get blog data from bin
    response = requests.get(url=BLOG_URL)
    response.raise_for_status()
    data = response.json()
    print("Obtained blog data")
    print(data)
    return data


@app.route('/')
def home():
    # Homepage for blog
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    return render_template("index.html", posts=blog_posts)


@app.route('/about.html')
def about():
    # About
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        subject = "Contact Form Received"
        content = "Name: " + str(data["name"]) + \
                  "\nE-Mail: " + str(data["email"]) + \
                  "\nPhone: " + str(data["phone"]) + \
                  "\nMessage: " + str(data["message"])
        # send_msg is the concatenation of subject and content
        send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')

        if sendgrid_enabled == 1:
            sendemail.send_grid_email(to_email, subject, content)
        else:
            sendemail.send_smtp_email(to_email, send_msg)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<num>')
def read_post(num):
    # Specific post
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    requested_post = []
    for i in blog_posts:
        if str(i["id"]) == str(num):
            requested_post = i
    print("Selected blog post")
    return render_template("post.html", posts=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
