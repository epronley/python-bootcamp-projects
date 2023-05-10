# _________________________________SNAKE GAME______________________________ #
# Use WASD or Arrow Keys to move the snake around
# Collect food by moving the snake over it
# If player collides with wall, blocks, or self, it's game over
# Player collects 10 food to proceed to next level
# Once player reaches level 4 - they collect as much food as they can without dying
# High score is saved in the high_score.txt file

import snake as s
import turtle as t
import time
import food as f
import scoreboard as p
import level_manager as l

FOOD_GOAL = 10

# Create and setup Screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create Scoreboard and show start screen
scoreboard = p.Scoreboard()
scoreboard.display_start()


# _________________________________SHOW LEVEL______________________________ #
def show_level(level):
    scoreboard.clear()
    scoreboard.display_level(level)
    screen.update()
    scoreboard.update_score()
    time.sleep(2)


# _________________________________START GAME______________________________ #
def start_game():
    food_counter = 0
    level = 1

    # Clear Start Screen
    show_level(level)

    # Initialize important variables, create game objects, and turn game on
    game_is_on = True
    snake = s.Snake()
    food = f.Food()
    level_manager = l.LevelManager()
    level_manager.create_level(level)

    while game_is_on:
        snake.show()
        food.showturtle()
        level_manager.show_blocks()
        screen.update()
        time.sleep(0.1)

        # Move Snake
        snake.move()

        # Detect collision with food
        if snake.snake_body[0].distance(food) < 15:
            food_counter += 1
            food.refresh()
            for block in level_manager.blocks:
                if food.distance(block) < 20:
                    food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False

        # Detect collision with self
        for body in snake.snake_body[1:]:
            if snake.head.distance(body) < 10:
                game_is_on = False

        # Detect collision with blocks
        for block in level_manager.blocks:
            if snake.head.distance(block) < 20:
                game_is_on = False

        # Check end of level
        if food_counter == FOOD_GOAL and level != 4:
            food_counter = 0
            level += 1
            food.hideturtle()
            snake.hide()
            level_manager.hide_blocks()
            show_level(level)
            level_manager.create_level(level)
            snake.reset()

        # Listen to player input for snake
        screen.listen()
        screen.onkey(snake.up, "w")
        screen.onkey(snake.down, "s")
        screen.onkey(snake.left, "a")
        screen.onkey(snake.right, "d")
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

    scoreboard.check_score()
    scoreboard.display_game_over()


# Listen for player input
screen.listen()
screen.onkey(start_game, "Return")

screen.exitonclick()
