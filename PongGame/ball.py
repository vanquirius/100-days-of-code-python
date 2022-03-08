# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 22 - Pong Game

from turtle import Turtle

UPPER_LIMIT = 300
LOWER_LIMIT = 300

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)

    def move_ball(self, input_vertical_speed, input_horizontal_speed):
        # Bounce off top and lower walls
        if self.ycor() > UPPER_LIMIT or self.ycor() < -LOWER_LIMIT:
            input_vertical_speed *= -1
        # Move ball
        self.goto(self.xcor() + input_horizontal_speed, self.ycor() + input_vertical_speed)
        return input_vertical_speed, input_horizontal_speed