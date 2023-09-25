from turtle import Turtle
ALIGN="CENTER"
FONT=("Arial",22,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGN,font=FONT)

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GameOver",align=ALIGN,font=FONT)