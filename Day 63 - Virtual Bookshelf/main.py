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
from wtforms import StringField, SubmitField, SelectField, HiddenField
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


# Add new book form
class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = SelectField("Rating", choices=["*", "**", "***", "****", "*****"], validators=[DataRequired()])
    submit = SubmitField('Add Book')

# Edit book rating form
class EditRatingForm(FlaskForm):
    book_rating = SelectField("Rating", choices=["*", "**", "***", "****", "*****"], validators=[DataRequired()])
    submit = SubmitField('Change Rating')

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
        new_book = Book(
            title=form.book_name.data,
            author=form.book_author.data,
            rating=form.book_rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditRatingForm()
    if form.validate_on_submit():
        book_id = request.args.get('id')
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = form.book_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", form=form, book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
