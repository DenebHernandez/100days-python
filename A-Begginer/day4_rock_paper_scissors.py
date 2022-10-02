import random as rnd

#ASCI art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

weapons = [rock, paper, scissors]
#Game starting question
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

#Computer choice
computer_choice = rnd.randint(0,2)

if player_choice == computer_choice:
    winner = None
elif player_choice == 0:
    if computer_choice == 1:
        winner = "computer"
    else:
        winner = "player"
elif player_choice == 1:
    if computer_choice == 0:
        winner = "player"
    else:
        winner = "computer"
elif player_choice == 2:
    if computer_choice == 0:
        winner = "computer"
    else:
        winner = "player"

print(weapons[player_choice])
print(f"Computer chose:\n {weapons[computer_choice]}")
if winner == None:
    print("It's a tie")
elif winner == "player":
    print("You win")
else:
    print("You lose")