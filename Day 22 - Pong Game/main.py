# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 22 - Pong Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
import time
import random

# Ball speed increase over time
SPEED_INCREASE = 1.001
# Ball speed decrease when bouncing off paddle
SPEED_DECREASE = 0.999

# Screen size
width = 800
height = 600

# Create screen
screen = Screen()
screen.setup(width, height)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
wall = Wall.create_wall(width, height)

# Create paddles
right_paddle = Paddle("right")
left_paddle = Paddle("left")

# Start with no ball
ball_on_field = False

# Add scoreboard
right_scoreboard = Scoreboard(width, height, "right")
left_scoreboard = Scoreboard(width, height, "left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    # Get user input
    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")

    # Add a ball if there is no ball
    if not ball_on_field:
        ball = Ball()
        ball_on_field = True
        vertical_speed = random.randint(-10, 10)
        horizontal_speed = random.randint(-10, 10)
        if horizontal_speed == 0:
            horizontal_speed = 1

    # Keep ball moving
    vertical_speed, horizontal_speed = ball.move_ball(vertical_speed, horizontal_speed)
    vertical_speed *= SPEED_INCREASE
    horizontal_speed *= SPEED_INCREASE

    # Bounce off paddles
    if (ball.xcor() > 340 and ball.distance(right_paddle) < 50) or (
            ball.xcor() < -340 and ball.distance(left_paddle) < 50):
        horizontal_speed *= -1
        vertical_speed *= SPEED_DECREASE
        horizontal_speed *= SPEED_DECREASE

    # Check wall collision, add points
    # Right wall
    if ball.xcor() > (width / 2 - 25):
        left_scoreboard.add_point()
        ball.reset()
        ball_on_field = False
    # Left wall
    if ball.xcor() < (-width / 2 + 25):
        right_scoreboard.add_point()
        ball.reset()
        ball_on_field = False

screen.exitonclick()
