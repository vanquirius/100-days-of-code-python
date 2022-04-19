# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-17

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 64 - Top 10 Movies Website

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from sqlalchemy.exc import InvalidRequestError
from tmdb import MovieSearch

# Flask setup with CSRF Protection + Bootstrap + WTForms
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
csrf = CSRFProtect(app)
csrf.init_app(app)
Bootstrap(app)

# Setup Database with SQLAlchemy
FILE_URI = "sqlite:///movies.db"
app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI  # load the configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Significant overhead if True. Future default: False
db = SQLAlchemy(app)  # create the SQLAlchemy object by passing it the application


# Format for movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    # Optional: this will allow each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


# Create movie table
try:
    db.create_all()
except InvalidRequestError:
    pass


# Add new movie form
class MovieForm(FlaskForm):
    movie_name = StringField('Movie Name', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# Edit book rating form
class EditMovieForm(FlaskForm):
    movie_review = StringField("Your Review", validators=[DataRequired()])
    movie_rating = StringField("Your Rating out of 10", validators=[DataRequired()])
    submit = SubmitField('Change Rating')


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    # Capture movie name from the form
    if form.validate_on_submit():
        # Search movie name in TMDB (might be multiple results)
        movie_search = MovieSearch(form.movie_name.data).get_movie_data()
        print(movie_search)
        return render_template('select.html', movie_search=movie_search)
    return render_template('add.html', form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.review = form.movie_review.data
        movie_to_update.rating = float(form.movie_rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", form=form, movie=movie_selected)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    # DELETE A RECORD BY ID
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
