from turtle import Screen, Turtle


# Adding some constants for readability
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20

class Snake:
    # As soon as Snake() is called, __init__ will run
    # In this case, it will create segments as well as create_snake()
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for x in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x)
            self.segments.append(new_segment)
    def move(self):
        # range(start = x, end = y, step = z)
        # we use len segments in case the number of segments change
        # this loop basically takes the tail, updates it to the next square and keeps doing that
        for seg_num in range(len(self.segments) - 1, 0, -1): 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_SPEED)