# _________________________________SNAKE CLASS______________________________ #
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    # _________________________________INITIALIZE______________________________ #
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # _________________________________CREATE SNAKE BODY______________________________ #
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # _________________________________ADD SEGMENT TO SNAKE______________________________ #
    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    # _________________________________RESET SNAKE______________________________ #
    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    # _________________________________EXTEND SNAKE______________________________ #
    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    # _________________________________HIDE SNAKE______________________________ #
    def hide(self):
        for body in self.snake_body:
            body.hideturtle()

    # _________________________________SHOW SNAKE______________________________ #
    def show(self):
        for body in self.snake_body:
            body.showturtle()

    # _________________________________MOVE SNAKE______________________________ #
    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # _________________________________SET SNAKE HEADING______________________________ #
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
