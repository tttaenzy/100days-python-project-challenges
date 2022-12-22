import turtle

import colorgram
import random
from turtle import Turtle, Screen

turtle.colormode(255)

colors = colorgram.extract('hirst.jpg', 20)

# below for-loop is used to extract rgb list of color produce with the help of colorgram Module with picture.
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     my_color.append(new_color)



tim = Turtle()
tim.penup()
tim.hideturtle()
my_color = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
            (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
            (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
            (106, 108, 198), (137, 29, 72)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dot=100
# change your object speed here
tim.speed('fastest')
for dot in range(1,num_dot+1):
    tim.dot(10, random.choice(my_color))
    tim.forward(50)
    if dot % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
my_screen = Screen()
my_screen.exitonclick()

