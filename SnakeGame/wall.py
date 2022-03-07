# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 20/21 - Snake Game

from turtle import Turtle


class Wall:

    def create_wall(input_width, input_height):
        wall_draw = Turtle()
        wall_draw.color("black")
        wall_draw.pencolor("white")
        wall_draw.penup()
        # Top Left corner
        wall_draw.goto(-input_width/2, +input_height/2)
        wall_draw.pendown()
        # Top Right corner
        wall_draw.goto(+input_width / 2, +input_height / 2)
        # Bottom Right corner
        wall_draw.goto(+input_width / 2, -input_height / 2)
        # Bottom Left corner
        wall_draw.goto(-input_width / 2, -input_height / 2)
        # Top Left corner
        wall_draw.goto(-input_width/2, +input_height/2)
        wall_draw.hideturtle()