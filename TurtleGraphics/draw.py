# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-06

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 18 - Turtle Graphics

import random
from turtle import Screen
import colorgram

class Draw:
    # draw a dashed line
    def dash(size, color, turtle):
        turtle.pencolor(color)
        turtle.color(color)
        for i in range(10):
            turtle.forward(size)
            turtle.penup()
            turtle.forward(size)
            turtle.pendown()

    # draw a shape
    def shape(size, sides, turtle):
        colors = {"red", "black", "blue", "green", "pink"}
        color = random.choice(list(colors))
        turtle.pencolor(color)
        turtle.color(color)
        angle = (360 / sides)
        for i in range(sides):
            turtle.forward(size)
            turtle.right(angle)

    # random walk
    def randomwalk(size, turtle):
        #colors = {"red", "black", "blue", "green", "pink"}
        i = 0
        while i < 200:
            # choose color from list
            # color = random.choice(list(colors))
            # random colors
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            screen = Screen()
            screen.colormode(255)
            turtle.pencolor(color)
            turtle.color(color)
            r = random.randint(1, 3)
            if r == 1:
                turtle.right(90)
            if r == 2:
                turtle.left(90)
            turtle.forward(size)
            i += 1

    # draw circle
    def circle(size, turtle):
      # random colors
      color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      screen = Screen()
      screen.colormode(255)
      turtle.pencolor(color)
      turtle.color(color)
      turtle.circle(size)
    
    # Hirst painting
    def paint(turtle):
      # get colors from image
      rgb_colors = []
      color_list = []
      colors = colorgram.extract('image.png', 30)
      for color in colors:
          r = color.rgb.r
          g = color.rgb.g
          b = color.rgb.b
          # do not include too close to white
          if (r > 240) and (g > 240) and (b > 240):
            pass
          else:
            new_color = (r, g, b)
            rgb_colors.append(color.rgb)
            color_list.append(new_color)
     
      print("Color list:")
      print(color_list)
      turtle.penup()
      turtle.setheading(225)
      turtle.forward(100)
      turtle.setheading(0)
      # paint 10 x 10 dots, 20 in size, spaced apart 50 units
      dot_count = 0
      turtle.hideturtle()
      while(dot_count < 100):
        for i in color_list:      
          if(dot_count < 100):
              screen = Screen()
              screen.colormode(255)
              turtle.pencolor(i)
              turtle.dot(size=20)
              turtle.forward(50)
              dot_count += 1
              if dot_count in (10, 20, 30, 40, 50, 60, 70, 80, 90):
                turtle.right(180)
                turtle.forward(500)
                turtle.right(90)
                turtle.forward(50)
                turtle.right(90)
      