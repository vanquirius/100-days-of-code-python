# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-06

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 18 - Turtle Graphics

#####Turtle Intro######

import turtle as t
from draw import Draw

#timmy_the_turtle = t.Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)

timmy = t.Turtle()

# Which challenge?
while True:
  challenge = input("Which challenge to execute?")

  ######## Challenge 1 - Draw a Square ############
  if challenge == "1":
    Draw.shape(100, 4, timmy)
  ######## Challenge 2 - Draw a Dashed Line########
  if challenge == "2":
      Draw.dash(10, "grey40", timmy)
  ######## Challenge 3 - Draw shapes ##############
  if challenge == "3":
    for i in range(4, 10):
      Draw.shape(100, i, timmy)
  ######## Challenge 4 - Random Walk ##############
  if challenge == "4":
    Draw.randomwalk(20, timmy)
  ######## Challenge 5 - Spirograph ###############
  if challenge == "5":
    for i in range(1,36):
      Draw.circle(100, timmy)
      timmy.right(10)
  ######## Challenge 6 - Hirst #### ###############
  if challenge == "6":
    Draw.paint(timmy)