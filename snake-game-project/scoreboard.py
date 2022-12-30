from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.color("white")
        self.setposition(0,280)
        self.write(f"Score: {self.score}", align="center", font=("Cooper Black", 15, "italic"))


    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align="center", font=("Cooper Black", 15, "italic"))


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("white")
        self.write(f"Game Over", align="center", font=("Cooper Black", 15, "italic"))



