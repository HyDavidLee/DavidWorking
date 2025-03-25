from turtle import Turtle

FONT = ("Consolas", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.write(f"{self.l_score}         {self.r_score}", align="center", font = FONT)

    def score(self, score):
        if(score == "left"):
            self.l_score += 1
            self.clear()
            self.update_scoreboard()
        else:
            self.r_score += 1
            self.clear()
            self.update_scoreboard()

    def game_over(self):
        winner = "Nobody"
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.write(f"Game over\nLeft Wins!!!", align="center", font=FONT)
        else:
            self.write(f"Game over\nRight Wins!!!", align="center", font=FONT)
    