# _________________________________SCOREBOARD CLASS______________________________ #
from turtle import Turtle


class Paddle(Turtle):

    # _________________________________INITIALIZE______________________________ #
    def __init__(self, player):
        """Set paddle position"""
        super().__init__()
        self.create_player()
        if player == 1:
            self.setx(350)
        else:
            self.setx(-360)

    # _________________________________CREATE PLAYER______________________________ #
    def create_player(self):
        """Create the player's paddle"""
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)

    # _________________________________MOVEMENT FUNCTIONS______________________________ #
    def move_up(self):
        pos = self.ycor()
        self.sety(pos + 20)

    def move_down(self):
        pos = self.ycor()
        self.sety(pos - 20)