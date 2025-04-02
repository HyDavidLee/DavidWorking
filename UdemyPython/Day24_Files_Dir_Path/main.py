from turtle import Screen, Turtle
import time

screen = Screen()

from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen.setup(700, 700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

cage = Turtle()
cage.pencolor("white")
cage.penup()
cage.goto(310, 310)
cage.pendown()
cage.goto(310, -310)
cage.goto(-310, -310)
cage.goto(-310, 310)
cage.goto(310, 310)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Detect collision with wall
    # removed game_is_on False to just resetting board
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    snake.move()

    # Detect Collision with food
    # we can use .distance, it checks what the distance between two turtles are
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        score.points()
    
    # detect collision with tail
    # if head collides with any segment in the tail
        # trigger game over
    # removed game_is_on False to just resetting board
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



score.lost()








screen.exitonclick()