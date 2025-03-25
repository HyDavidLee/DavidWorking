from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # detect collision with paddle
    # normally we would do .distance() and if its 20 away then it made contact
    # however, our paddle is not a square, there is a y axis
    # to solve this, we can add a a constraint of an invisible wall vertically to take care of all things past that
    # then we can say if its within a 50 pixel range then we're good
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()

    if ball.xcor() > 400 and ball.distance(r_paddle) > 50:
        scoreboard.score("left")
        ball.ball_reset()
    if ball.xcor() < -400 and ball.distance(l_paddle) > 50:
        scoreboard.score("right")
        ball.ball_reset()

    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()