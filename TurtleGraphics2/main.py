# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-13

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 19 - Turtle Graphics 2

from turtle import Turtle, Screen
import random

# Etch-a-Sketch
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def move_clockwise():
    tim.right(5)

def move_counterclockwise():
    tim.left(5)

def reset_screen():
    tim.clear()
    tim.reset()

def etch_a_sketch():
  screen = Screen()
  screen.listen()
  screen.onkey(key="w", fun=move_forwards)
  screen.onkey(key="s", fun=move_backwards)
  screen.onkey(key="d", fun=move_clockwise)
  screen.onkey(key="a", fun=move_counterclockwise)
  screen.onkey(key="c", fun=reset_screen)
  screen.exitonclick()

def turtle_race():
  screen = Screen()
  screen.setup(width = 500, height = 200)
  # Select turtle to bet
  bet = ""
  while bet not in ("red", "green", "blue", "yellow", "purple"):
    bet = screen.textinput(title = "Make your bet", prompt = "Which color of turtle will win?")

  # Create turtles
  def create_turtle(input_color, input_y_pos):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(input_color)
    turtle.setpos(x = -200, y = input_y_pos)
    return turtle
  
  red_turtle = create_turtle("red", -80)
  green_turtle = create_turtle("green", -50)
  blue_turtle = create_turtle("blue", -20)
  yellow_turtle = create_turtle("yellow", 10)
  purple_turtle = create_turtle("purple", 40)
  turtles = [red_turtle, green_turtle, blue_turtle, yellow_turtle, purple_turtle]

  def random_forward(turtle):
    turtle.forward(random.randint(1, 3))
  
  race = 1
  while race == 1:
    for i in turtles:
      random_forward(i)
      if i.xcor() == 250:
        race = 0
        won_color = i.color()[0]
        print("Turtle " + str(won_color) + " won the race!")
        if won_color == bet:
          print("You won!")
        else:
          print("You lost!")

  screen.exitonclick()

# Runtime

# Which challenge?
challenge = input("Which challenge to execute?")

if challenge == "1":
  tim = Turtle()
  etch_a_sketch()

if challenge == "2":
  turtle_race()