# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 20/21 - Snake Game

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, input_width, input_height):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh(input_width, input_height)

    def refresh(self, input_width, input_height):
        x_coord = random.randint(round(-input_width/2)+10,round(input_width/2)-10)
        y_coord = random.randint(round(-input_height/2)+10,round(input_height/2)-10)
        self.goto(x_coord, y_coord)