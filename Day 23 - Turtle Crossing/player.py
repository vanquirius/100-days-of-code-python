# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 23 - Turtle Crossing

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.back_to_start()
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)