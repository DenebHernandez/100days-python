# Hangman game
from operator import le
import random

word_list= ["camel", "baboon", "guitar", "test", "castle", "jiraffe", "tree"]

#Welcome message and pregame settings
print("welcome to the hangman game")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)


# List for displaying the word and guessed characters
display = []
for i in range(word_length):
    display += "_"

lives = 5

while lives > 0:
    current_display = "".join(display)
    if current_display != chosen_word:

        print("".join(display))
        guess = input("Guess a letter: ").lower()

        correct_letter = False

        # Check if guess was correct 
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
                correct_letter = True
        
        if not correct_letter:
            lives -= 1
        print(f"You have {lives} lives left")