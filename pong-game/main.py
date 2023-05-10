# _________________________________PONG GAME______________________________ #
# Classic pong game
# Left player controls paddle with "W" and "S"
# Right player controls paddle with "UP" and "DOWN" arrow keys

# Import different classes and time module
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create and setup window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create ball, scoreboard, and players
ball = Ball()
scoreboard = Scoreboard()
player1 = Paddle(1)
player2 = Paddle(2)

# Listen for inputs
screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")

screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

# _________________________________MAIN CODE______________________________ #
game_is_on = True
while game_is_on:
    # Update screen/window every second and move ball
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # Detect collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -335:
        ball.bounce("x")

    # Detect when ball passes paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart(direction="l")
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.restart(direction="r")


screen.exitonclick()