# Hangman game
import random
from day6_hangman_words import word_list
from day6_hangman_art import stages, logo

#Welcome message and pregame settings
print(logo)
print("Welcome to the hangman game")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# List for displaying the word and guessed characters
display = []
for i in range(word_length):
    display += "_"

lives = 6
end_of_game = False
current_display = ''.join(display)

while not end_of_game:

    print(stages[lives])
    print(current_display)
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()

    # Check if guess was correct 
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        current_display = ''.join(display)
        if current_display == chosen_word:
            end_of_game = True
    else:
        lives -= 1
        if lives == 0:
            end_of_game = True


if current_display == chosen_word:
    print("You have won")
    print(f"The right word is {chosen_word}")
else:
    print(stages[lives])
    print(f"{''.join(display)}")
    print(f"You have lost, the right word was {chosen_word}")