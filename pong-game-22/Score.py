from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.first_score = 0
        self.second_score = 0
        self.penup()


class FirstScore(Score):
    def __init__(self):
        super().__init__()
        self.setposition(100, 280)
        self.write(f"Score: {self.first_score}", align="center", font=("Cooper Black", 15, "italic"))

    def increase_score(self):
        self.clear()
        self.first_score += 1
        self.setposition(100, 280)
        self.write(f"Score: {self.first_score}", align="center", font=("Cooper Black", 15, "italic"))


class SecondScore(Score):
    def __init__(self):
        super().__init__()
        self.setposition(-100, 280)
        self.write(f"Score: {self.second_score}", align="center", font=("Cooper Black", 15, "italic"))

    def increase_score(self):
        self.clear()
        self.second_score += 1
        self.setposition(-100, 280)
        self.write(f"Score: {self.second_score}", align="center", font=("Cooper Black", 15, "italic"))




