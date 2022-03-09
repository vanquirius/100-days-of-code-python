# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 23 - Turtle Crossing

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-250, 250))

    def move_left(self, input_level):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT*input_level, self.ycor())
        if self.xcor() < -320:
            self.goto(320, random.randint(-250, 250))