from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over\nYou got squished by a car get fucked LMAO\nScore = {self.level}\nContinue? (Y/N)", align="center", font=FONT2)
