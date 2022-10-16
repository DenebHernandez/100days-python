from functions import blackjack, cls
from art import card, suits, flipped_card

cls()

while input("Do you want to play a game of blackjack? Type 'y' to play: \n") == "y":
    blackjack()