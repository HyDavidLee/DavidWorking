from turtle import Turtle

FONT = ("Consolas", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(0, 260)
        self.penup()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)


    def points(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def lost(self):
        self.goto(0,0)
        self.write(f"You lose\nScore: {self.score}", align="center", font=FONT)