# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-22

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 68 - Authentication with Flask

import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
import secrets

# Start-up flask app
app = Flask(__name__)
# csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(250)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


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
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Sign me up")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    # Every render_template has a logged_in variable set.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        try:
            new_user = User(
                email=form.email.data,
                # Store password with hash/salt
                password=werkzeug.security.generate_password_hash(
                    form.password.data, method='pbkdf2:sha256', salt_length=8),
                name=form.name.data
            )
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError:
            return render_template("register.html", form=form, logged_in=current_user.is_authenticated)

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for("secrets"))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


def is_safe_url(next):
    pass


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        # E-mail doesn't exist
        if not user:
            flash("That e-mail does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # E-mail exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", form=form)


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory('static', filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
