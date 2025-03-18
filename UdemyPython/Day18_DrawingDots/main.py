import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('Dots.PNG', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)


random.shuffle(rgb_colors)
turt = Turtle()
t.colormode(255)

x_coor = 0
y_coor = 0
index = 0
for x in rgb_colors:
    turt.teleport(x_coor, y_coor)
    turt.pendown()
    turt.dot(50, x)
    turt.penup()
    if (index+1)%6 == 0:
        y_coor += 70
        x_coor = 0
    else: 
        x_coor += 70
    index += 1







screen = Screen()
screen.exitonclick()