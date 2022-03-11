# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 25 - US States Game

from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Statename(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.score = 0
        self.color("black")
        self.goto(x, y)
        self.write_score(state)

    def write_score(self, state):
        self.clear()
        self.write(str(state))
        self.hideturtle()