COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        self.all_car=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_number=random.randint(1,6)
        if random_number==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_y=random.randint(-220,220)
            random_color=random.choice(COLORS)
            new_car.color(random_color)
            new_car.penup()
            new_car.goto(300,random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT