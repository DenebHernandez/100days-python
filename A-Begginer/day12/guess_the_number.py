import random
import os
from art import logo

#Functions
#Clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Set difficulty level
def game_mode():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #Easy mode has 10 attempts at guessing the right number
    if user_input.lower() == "easy":
        return 10
    #Hard mode has 5 attempts at guessing the right number
    elif user_input.lower() == "hard":
        return 5
    else:
        print("\nInvalid input\n")
        return game_mode()

def game():
    end_game = False

    #Pick a random number from 1 to 100
    rand_number = random.randint(1,100)

    #Define the amount of guesses
    guess_amount = game_mode()

    #Game loop. Ask for user guess n times untill guess is right or ran out of attempts
    while not end_game:

        print(f"You have {guess_amount} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
        cls()

        #Check if guess is int
        if user_guess.isdigit():
            user_guess = int(user_guess)

            #Compare guess to random number
            if user_guess == rand_number:
                print(f"You won! the number is {rand_number}")
                end_game = True
            else:
                if user_guess < rand_number:
                    print("Too low\nGuess again")
                else:
                    print("Too high\nGuess again")
                guess_amount -= 1
        else:
            print("\nInvalid input, please guess a number\n")
        if guess_amount == 0:
            print(f"You ran out of attempts! the number was {rand_number}")
            end_game = True

#Welcome message
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game()
