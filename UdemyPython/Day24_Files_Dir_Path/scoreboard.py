from turtle import Turtle

FONT = ("Consolas", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("high score.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.penup()
        self.update_scoreboard()
        
    # Removed lost and game over screen and moved the functionality into update_scoreboard and call it here
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)

    # Removed lost and game over screen and moved the functionality into update_scoreboard and call it here
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def points(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()