from turtle import Screen
from paddle import  FirstP, SecondP
from ball import Ball
from Score import Score,FirstScore,SecondScore
import time

screen = Screen()
screen.title("Pong game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

first_paddle = FirstP()
second_paddle = SecondP()
ball=Ball()
score=Score()
first_score=FirstScore()
second_score=SecondScore()




screen.listen()
screen.onkeypress(first_paddle.up, "Up")
screen.onkeypress(first_paddle.down, "Down")
screen.onkeypress(second_paddle.up,"w")
screen.onkeypress(second_paddle.down,"x")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect collision with up wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #     detect collition with both paddle
    elif ball.distance(first_paddle) <50 and ball.xcor()>320 or ball.distance(second_paddle) < 50 and ball.xcor() <-310:
        ball.bounce_x()

#     detect collision with right border
    elif ball.xcor()>380:
        second_score.increase_score()
        ball.reset_position()

    #     detect collition with left border
    elif ball.xcor() < -380:
        first_score.increase_score()
        ball.reset_position()





screen.exitonclick()
