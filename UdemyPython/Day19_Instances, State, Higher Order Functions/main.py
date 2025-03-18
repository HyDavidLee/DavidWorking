from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_up():
    tim.setheading(90)
    tim.forward(10)
def move_down():
    tim.setheading(270)
    tim.forward(10)
def move_right():
    tim.setheading(0)
    tim.forward(10)
def move_left():
    tim.setheading(180)
    tim.forward(10)


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_down, "Down")

screen.exitonclick()