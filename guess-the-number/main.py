# Allows the player to submit a guess for a number between 1 and 100.
# Checks the user's guess against actual answer.
# Prints "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, it shows the actual answer to the player.
# Tracks the number of turns remaining.
# If they run out of turns, provides feedback to the player.
# Includes two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import art and random module
from art import logo
import random

# Print game logo
print(logo)

# Set main variables
guesses = 0
question_answered = False

# Welcome player to game
print("Welcome to Number Game!")


# _______________________________GUESS NUMBER FUNCTION_____________________________________ #
def guess_number(guess, number):
    """Player guesses a number and it returns whether the guess is high, low, or correct"""
    if guess > number:
        return "High"
    if guess < number:
        return "Low"
    if guess == number:
        return "win"


# _______________________________PLAY GAME FUNCTION_____________________________________ #
def play_game(guesses):
    """Starts the game by picking a number and asking the player for a guess."""
    # Set function variables
    number = random.randint(1, 100)
    game_over = False

    # Play game
    print(f"I've picked a number between 1 and 100. You have {guesses} guesses to get it right.")
    while not game_over:
        guess = int(input("Pick a number between 1 and 100\n"))
        answer = guess_number(guess, number)
        if answer == "Low" or answer == "High":
            guesses -= 1
            print(f"Too {answer}.")
        elif answer == "win":
            print(f"{number} is correct! You Win!")
            game_over = True
            return
        if guesses == 0:
            print(f"The number was {number}")
            print("You're out of guesses. Game over.")
            game_over = True
        elif guesses == 1:
            print("You have 1 guess left.")
        elif guesses > 0:
            print(f"You have {guesses} guesses left.")


# _______________________________MAIN CODE/PICK DIFFICULTY_____________________________________ #
while not question_answered:
    choice = input("Would you like 'Easy' or 'Hard' mode?\n").lower()
    if choice == 'easy':
        guesses = 10
        question_answered = True
        play_game(guesses)
    elif choice == 'hard':
        guesses = 5
        question_answered = True
        play_game(guesses)
    else:
        print("That's not an option.")



