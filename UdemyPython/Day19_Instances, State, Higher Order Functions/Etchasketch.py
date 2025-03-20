from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

degrees = 0

def move_up():
    tim.forward(10)
def move_down():
    global degrees
    degrees -= 180
    tim.setheading(degrees)
def turn_right():
    global degrees
    degrees -= 10
    tim.setheading(degrees)
def turn_left():
    global degrees
    degrees += 10
    tim.setheading(degrees)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(turn_right, "Right")
screen.onkey(turn_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(clear, "c")

screen.exitonclick()