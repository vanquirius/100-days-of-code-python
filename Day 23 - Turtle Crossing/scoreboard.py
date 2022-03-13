# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 23 - Turtle Crossing

ALIGN = "center"
FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.score = 0
        self.color("black")
        self.goto(-width/2 + 0.15*width, height/2 - 0.08*height)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write('Level: ' + str(self.score), font=FONT, align=ALIGN)
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.write_score()

    def current_score(self):
        return self.score

    def game_over(self):
        self.goto(0 ,0)
        self.write('GAME OVER', font=FONT, align=ALIGN)
