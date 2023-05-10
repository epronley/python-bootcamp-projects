# _________________________________BLACKJACK HOUSE RULES______________________________ #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Import random and art
import random
from art import logo

# Create main variables of deck and starting money
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money = 1000


# _________________________________HIT FUNCTION______________________________ #
def hit(hand):
    """Give the player or computer another card."""
    hand.append(random.choice(deck))
    return hand


# _________________________________DEAL FUNCTION______________________________ #
def deal(player_money, player_bet):
    """Deal the cards to the player and to the computer. Starts new round."""
    print(logo)
    player_stands = False
    player_hand = []
    computer_hand = []
    for i in range(2):
        player_hand.append(random.choice(deck))
    for i in range(2):
        computer_hand.append(random.choice(deck))
    computer_hand_display = [computer_hand[0], "?"]

    print(f"Your cards are {player_hand}. A total of {sum(player_hand)}")
    print(f"The dealer's cards are {computer_hand_display}")
    while not player_stands:
        hit_or_pass = input("Would you like to hit or stand? 'Hit' or 'Stand'\n").lower()

        if hit_or_pass == 'hit':
            player_hand = hit(player_hand)
            if sum(player_hand) > 21:
                print(f"Your hand {player_hand} is over 21. You lose ${player_bet}")
                player_money -= player_bet
                player_stands = True
                if player_money > 0:
                    play_again(player_money)
                else:
                    print("You are out of money!")
                    print("Goodbye!")
            else:
                print(f"Your new hand is {player_hand}, a total of {sum(player_hand)}.")
        else:
            player_stands = True
            print(f"The dealer's full hand is {computer_hand}")
            while sum(computer_hand) < 21:
                hit(computer_hand)
                print(computer_hand)
            if 21 >= sum(computer_hand) > sum(player_hand):
                print(
                    f"Dealer Wins with a total of {sum(computer_hand)} compared to your hand of "
                    f"{sum(player_hand)}. You Lose ${player_bet}.")
                player_money -= player_bet
                if player_money > 0:
                    play_again(player_money)
                else:
                    print("You are out of money!")
                    print("Goodbye!")
            elif sum(computer_hand) > 21:
                print(f"The dealer busts at a total of {sum(computer_hand)}. You win ${player_bet}!")
                player_money += player_bet
                play_again(player_money)
            elif sum(computer_hand) == sum(player_hand):
                print(f"It's a tie! And tie goes to the house, so - you lose ${player_bet}")
                player_money -= player_bet
                play_again(player_money)


# _________________________________PLAY AGAIN FUNCTION______________________________ #
def play_again(player_money):
    """Ask the player if they'd like to play again."""
    print(f"Your new total of money is: ${player_money}")
    choice = input("Would you like to play again? 'Y' or 'N'\n").lower()
    if choice == 'y':
        player_bet = int(input("How much would you like to bet?\n"))
        deal(player_money, player_bet)
    else:
        print(f"Your total money is: ${player_money}")
        print("Goodbye!")


# _________________________________MAIN CODE_____________________________ #
play_a_game = input("Would you like to play a game of blackjack? 'Y' or 'N'\n").lower()
if play_a_game == 'y':
    print(f"You have ${money}")
    bet = int(input("How much would you like to bet?\n"))
    deal(money, bet)
else:
    print("Then what are you doing here?")
    print("Goodbye")
