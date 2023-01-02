FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.hideturtle()
        self.goto(-250, 250)
        self.level()

    # this function will show your current level
    def level(self):
        self.clear()
        self.write(f"Level= {self.score}", font=FONT)

    # this function will increase level
    def increase(self):
        self.score += 1
        self.level()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("Game Over 😭", align="center", font=("Courier", 50, "normal"))
