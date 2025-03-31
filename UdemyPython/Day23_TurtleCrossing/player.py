from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create the turtle
# On up command turtle moves up
# Needs to reset back to bottom if turtle makes it across safely

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_bottom(self):
        self.goto(STARTING_POSITION)