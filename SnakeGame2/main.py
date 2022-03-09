# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 20/21 - Snake Game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time

# Screen size
width = 900
height = 900

# Create screen
screen = Screen()
screen.setup(width, height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
wall = Wall.create_wall(width, height)

# Create snake, food and scoreboard objects
snake = Snake()
food = Food(width, height)
scoreboard = Scoreboard(width, height)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Get user input
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Detect eating food
    if snake.head.distance(food) < 15:
        food.refresh(width, height)
        scoreboard.add_point()
        snake.extend()

    # Check wall collision
    if snake.head.xcor() > (width / 2 - 5) or snake.head.xcor() < (-width / 2 + 5) or snake.head.ycor() > (
            height / 2 - 5) or snake.head.ycor() < (-height / 2 + 5):
        print("Wall collision, game over!")
        scoreboard.reset()
        snake.reset()

    # Check collision with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 1:
            print("Tail collision, game over!")
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
