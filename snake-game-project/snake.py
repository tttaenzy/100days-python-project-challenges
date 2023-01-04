from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP=90
RIGHT=0
DOWN=270
LEFT=180


class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_segment= []
        for position in STARTING_POSITION:
           self.add_segment(position)


    def reset(self):
        for seg in self.snake_segment:
            seg.goto(1000,1000)
        self.snake_segment.clear()
        for position in STARTING_POSITION:
           self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segment.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)

        self.snake_segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segment[0].heading()!=DOWN:
            self.snake_segment[0].setheading(UP)

    def down(self):
        if self.snake_segment[0].heading() != UP:
            self.snake_segment[0].setheading(DOWN)

    def right(self):
        if self.snake_segment[0].heading() != LEFT:
            self.snake_segment[0].setheading(RIGHT)

    def left(self):
        if self.snake_segment[0].heading() != RIGHT:
            self.snake_segment[0].setheading(LEFT)
