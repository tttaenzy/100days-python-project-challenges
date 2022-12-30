from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Gameover

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collition with food

    if snake.snake_segment[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()
    # detect collition with border
    elif snake.snake_segment[0].xcor()>280 or snake.snake_segment[0].xcor()< -280 or snake.snake_segment[0].ycor()>280 or snake.snake_segment[0].ycor()< -280:
        game_is_on=False
        gameover=Gameover()
#     detect collition with tail or body of snake
    for segment in snake.snake_segment[1:]:
        # if segment==snake.snake_segment[0]:
        #     pass
        # elif snake.snake_segment[0].distance(segment)<10:
        #     game_is_on=False
        #     gameover=Gameover()
        if snake.snake_segment[0].distance(segment)<10:
            game_is_on=False
            gameover=Gameover()



screen.exitonclick()
