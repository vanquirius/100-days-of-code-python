# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 23 - Turtle Crossing

FINISH_LINE_Y = 280
NUMBER_OF_CARS = 10

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from wall import Wall

# Screen size
width = 600
height = 600

# Create screen
screen = Screen()
screen.setup(width, height)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)
wall = Wall.create_wall(width, height)

# Add scoreboard
scoreboard = Scoreboard(width, height)

# Add player
player = Player()

# Create cars
car_array = []
for i in range(0, NUMBER_OF_CARS):
    new_car = CarManager()
    car_array.append(new_car)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    # Get user input
    screen.listen()
    screen.onkey(player.up, "Up")

    # Move cars
    for car in car_array:
        car.move_left(scoreboard.current_score())

    # Check car collision with player
    for car in car_array:
        if player.distance(car) < 15:
            #player.back_to_start()
            scoreboard.game_over()
            game_is_on = False

    # Check wall collision, add points
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.add_point()
        player.back_to_start()

screen.exitonclick()
