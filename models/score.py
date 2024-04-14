from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 260)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.write_score()
