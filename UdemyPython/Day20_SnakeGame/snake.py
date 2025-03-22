from turtle import Screen, Turtle


# Adding some constants for readability
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    # As soon as Snake() is called, __init__ will run
    # In this case, it will create segments as well as create_snake()
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in STARTING_POSITION:
            self.add_segment(x)

    def move(self):
        # range(start = x, end = y, step = z)
        # we use len segments in case the number of segments change
        # this loop basically takes the tail, updates it to the next square and keeps doing that
        for seg_num in range(len(self.segments) - 1, 0, -1): 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def add_segment(self, x):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # using -1, we are effectively grabbing the last segment of our snake

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
