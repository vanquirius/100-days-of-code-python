# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 22 - Pong Game

from turtle import Turtle

MOVE_DISTANCE = 50
UPPER_LIMIT = 260
LOWER_LIMIT = 260


class Paddle(Turtle):

    def __init__(self, paddle_side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if paddle_side == "right":
            xcor = 350
        if paddle_side == "left":
            xcor = -350
        self.goto(xcor, 0)

    def up(self):
        if self.ycor() < UPPER_LIMIT:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -LOWER_LIMIT:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
