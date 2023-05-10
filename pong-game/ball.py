# _________________________________BALL CLASS______________________________ #
from turtle import Turtle


class Ball(Turtle):
    # Create main variables
    SPEED = 10
    x_speed = SPEED
    y_speed = SPEED

    # _________________________________INITIALIZE______________________________ #
    def __init__(self):
        """Create the ball."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.1

    # _________________________________MOVE FUNCTION_____________________________ #
    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.setpos(new_x, new_y)

    # _________________________________BOUNCE FUNCTION_____________________________ #
    def bounce(self, direction):
        """Ball will move after it comes into contact with paddle or wall"""
        if direction == "y":
            self.y_speed *= -1
        elif direction == "x":
            self.x_speed *= -1
            self.move_speed *= 0.9

    # _________________________________RESTART FUNCTION_____________________________ #
    def restart(self, direction):
        self.setpos(0, 0)
        if direction == "r":
            self.move_speed = 0.1
            self.y_speed = self.SPEED
            self.x_speed = self.SPEED
        elif direction == "l":
            self.move_speed = 0.1
            self.y_speed = -self.SPEED
            self.x_speed = -self.SPEED
