from turtle import Turtle,Screen
import random

screen=Screen()
user_choice=screen.textinput(title='WELCOME TO TURTLE RACE🐢🏁',prompt='Choose your turtle.(red, blue, black, pink):')
screen.setup(width=500,height=400)
is_race_on=False

# def start(turtle,angle,forward,turn_around):
#     turtle.shape('turtle')
#     turtle.speed('slow')
#     turtle.right(angle)
#     turtle.penup()
#     turtle.forward(forward)
#     turtle.left(turn_around)

def start(turtle,x,y):
    turtle.shape('turtle')
    turtle.speed('slow')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

# turtle 1
timmy=Turtle()
timmy.color('red')
# start(timmy,155,270,160)
start(timmy,x=-230,y=-100)



# turtle 2
tommy=Turtle()
tommy.color('blue')
# start(tommy,165,255,170)
start(tommy,x=-230,y=-50)

# turtle 3
sommy=Turtle()
sommy.color('black')
# start(sommy,180,245,180)
start(sommy,x=-230, y=0)

# turtle 4
tenzin=Turtle()
tenzin.color('pink')
# start(tenzin,190,250,190)
start(tenzin,x=-230,y=50)
turtles=[timmy,tommy,sommy,tenzin]

if user_choice:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_choice:
                print(f"You won the race!🏆 {winning_color} turtle is the winner.")
            else:
                print("you lost the race.😭")
                print(f"{winning_color} turtle won the race")
        random_distance=random.randint(0,10)
        turtle.penup()
        turtle.forward(random_distance)


# this is method to end my turtle race screen
screen.exitonclick()

