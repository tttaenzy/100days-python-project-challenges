import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard,GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    #     detect player collision with car
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            gameover=GameOver()

# detect if player reached the up level
    if player.ycor() > 230:
        score.increase()
        player.reset()
        car_manager.level_up()





screen.exitonclick()
