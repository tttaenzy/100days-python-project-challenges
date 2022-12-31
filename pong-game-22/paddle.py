from turtle import Turtle

UP = 90
DOWN = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    # def move(self):
    #     self.forward(20)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class FirstP(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=350, y=0)


class SecondP(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-350, y=0)
