# _________________________________HANGMAN GAME______________________________ #
# Computer picks random word from list
# Player guesses a letter
# If letter correct, it gets added to the mystery word
# If letter incorrect, the image of the hangman changes
# If player gets all letters, they win
# If player doesn't get the word before the hangman is finished, they lose

# Import random module, art, and list of words
import random
import hangman_art
import hangman_words

# Choose word and set length
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Create main variables
end_of_game = False
lives = 6

# Print Logo
print(hangman_art.logo)

# For testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blank lists
display = []
guesses = []

# Display hidden word
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

# _________________________________START GAME______________________________ #
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Add guess to list of guesses
    guesses += guess

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"Sorry, '{guess}' isn't in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The word was '{chosen_word}'")
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"\nGuesses: {guesses}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the hangman
    print(hangman_art.stages[lives])
