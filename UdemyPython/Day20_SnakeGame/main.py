from turtle import Screen, Turtle
import time

screen = Screen()

from snake import Snake


screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


serp = Snake()

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    serp.move()










screen.exitonclick()