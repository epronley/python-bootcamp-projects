# _________________________________SCOREBOARD CLASS______________________________ #
from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    start_game = False

    # _________________________________INITIALIZE______________________________ #
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.update_score()

    # _________________________________DISPLAY GAME START SCREEN______________________________ #
    def display_start(self):
        self.goto(0, 0)
        self.write(f"   Welcome to SNAKE\nPress 'Enter' to play!", False, ALIGNMENT, FONT)

    # _________________________________DISPLAY GAME OVER SCREEN______________________________ #
    def display_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    # _________________________________DISPLAY CURRENT LEVEL______________________________ #
    def display_level(self, level):
        self.goto(0, 0)
        self.write(f"Level {level}", False, ALIGNMENT, FONT)

    # _________________________________UPDATE SCORE______________________________ #
    def update_score(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, ALIGNMENT, FONT)

    # _________________________________CHECK AND WRITE SCORE______________________________ #
    def check_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

    # _________________________________INCREASE SCORE______________________________ #
    def increase_score(self):
        self.score += 1
        self.update_score()

