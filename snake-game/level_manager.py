# _________________________________LEVEL MANAGER CLASS______________________________ #
from turtle import Turtle

# Coordinates for the blocks of each level
LEVEL_TWO = {(150, 70), (150, 50), (150, 30),
             (-150, 70), (-150, 50), (-150, 30)}
LEVEL_THREE = {(200, 160), (200, 90), (200, 20),
               (-200, 160), (-200, 90), (-200, 20),
               (100, -50), (-100, -50)}
LEVEL_FOUR = {(200, 190), (200, 120), (-200, 190),
              (-200, 120), (150, 50), (-150, 50),
              (150, 30), (-150, 30), (50, 30),
              (-50, 30), (40, -100), (-40, -100),
              (40, -250), (-40, -250)}


class LevelManager:
    # _________________________________INITIALIZE______________________________ #
    def __init__(self):
        """Create blocks and set them outside the window"""
        self.blocks = []
        for i in range(20):
            block = Turtle("square")
            block.penup()
            block.goto(1000, 1000)
            block.hideturtle()
            self.blocks.append(block)

    # _________________________________HIDE BLOCKS______________________________ #
    def hide_blocks(self):
        for block in self.blocks:
            block.hideturtle()

    # _________________________________SHOW BLOCKS______________________________ #
    def show_blocks(self):
        for block in self.blocks:
            block.showturtle()

    # _________________________________CREATE LEVEL______________________________ #
    def create_level(self, level):
        match level:
            case 1:  # Level 1
                pass
            case 2:  # Level 2
                for block in self.blocks:
                    block.color("blue")
                    block.showturtle()
                i = 0
                for coordinate in LEVEL_TWO:
                    self.blocks[i].goto(tuple(coordinate))
                    i += 1
            case 3:  # Level 3
                for block in self.blocks:
                    block.color("red")
                i = 0
                for coordinate in LEVEL_THREE:
                    self.blocks[i].goto(tuple(coordinate))
                    i += 1
            case 4:  # Level 4
                for block in self.blocks:
                    block.color("yellow")
                i = 0
                for coordinate in LEVEL_FOUR:
                    self.blocks[i].goto(tuple(coordinate))
                    i += 1
