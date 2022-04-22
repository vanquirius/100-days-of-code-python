# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-22

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 68 - Authentication with Flask

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import InvalidRequestError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
try:
    db.create_all()
except InvalidRequestError:
    pass


# WTForm
class RegisterUser(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        pass
        return render_template('index.html')
    return render_template("register.html", form=form)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
