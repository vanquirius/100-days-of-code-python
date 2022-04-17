# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-17

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 63 - Virtual Bookshelf

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import InvalidRequestError

# Flask setup with CSRF Protection + Bootstrap + WTForms
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret123'
csrf = CSRFProtect(app)
csrf.init_app(app)
Bootstrap(app)

# Setup Database with SQLAlchemy
FILE_URI = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI  # load the configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Significant overhead if True. Future default: False
db = SQLAlchemy(app)  # create the SQLAlchemy object by passing it the application


# Format for book table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create book table
try:
    db.create_all()
except InvalidRequestError:
    pass

# Form template
class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = SelectField("Rating", choices=["*", "**", "***", "****", "*****"], validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    # Read list of books from database
    all_books = db.session.query(Book).all()
    # Render template with the most up-to-date list of books
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    # Capture data from the form and add to book list
    if form.validate_on_submit():
        new_book = {
            "title": form.book_name.data,
            "author": form.book_author.data,
            "rating": form.book_rating.data
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
