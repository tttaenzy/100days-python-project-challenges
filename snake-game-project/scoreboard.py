from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.setposition(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center",
                   font=("Cooper Black", 15, "italic"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("white")
        self.write(f"Game Over", align="center", font=("Cooper Black", 15, "italic"))
