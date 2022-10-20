import os
import random
from art import logo, vs
from game_data import data

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def pick_account():
    '''Picks a random Instagram account from the game data list'''
    account = random.choice(data)
    return account

def reassign_accounts(account_a, account_b, higher_account):
    # Move position b to a if higher account is b
    if higher_account == "b":
        account_a = account_b
    
    # Pick new value for b
    account_b = pick_account()

    # Checks in case a is equal to b and reassigns new account to b untill they are different
    while account_a == account_b:
        account_b = pick_account()

    return [account_a, account_b]

# Get user guess
def user_guess():
    # Get user guess
    guess = input("\nWho has more followers? Type 'A' or 'B': ")
    guess = guess.lower()
    # Check if guess is valid
    if not guess in ("a", "b"):
        print("\nInvalid guess\n")
        return user_guess()
    else:
        return guess

def check_guess(a_score, b_score, guess):
    # Check which account has a higher follower count
    if a_score > b_score:
        higher = "a"
    else:
        higher = "b"
    # Check answer
    if higher == guess:
        result = True
    else: 
        result = False
    
    return { "Result": result, "Higher": higher}

def higher_lower():
    # Initial values
    game_end = False
    score = 0

    # Asign account to position a or b
    account_a = pick_account()
    account_b = pick_account()
    while account_a == account_b:
        account_b = pick_account()
    
    # Welcome message
    cls()
    print(logo)
    print("\nWelcome to HIGHER/LOWER the game\n")

    # Game loop
    while not game_end:
        print(f'Compare A: {account_a["name"]}, a {account_a["description"]}, from {account_a["country"]}.')
        print(vs)
        print(f'Against B: {account_b["name"]}, a {account_b["description"]}, from {account_b["country"]}.')
        guess = user_guess()
        result = check_guess(a_score=account_a["follower_count"], b_score=account_b["follower_count"], guess=guess)
        if result["Result"]:
            score += 1
            cls()
            print(f"{logo}\nYou're right! Current score: {score}\n")
            new_accounts = reassign_accounts(account_a=account_a, account_b=account_b, higher_account=result["Higher"])
            account_a = new_accounts[0]
            account_b = new_accounts[1]
        else:
            cls()
            print(f"{logo}\nSorry, that's wrong. Final score: {score}")
            game_end = True
