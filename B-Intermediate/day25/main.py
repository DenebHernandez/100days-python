import os
import pandas as pd
import turtle as t

#define working directories
main_dir = os.getcwd() #100daysofpython folder
cwd = f"{main_dir}\B-Intermediate\day25" #access current day inside the main folder

#import game data and define game variables ans constants
game_data = pd.read_csv(f"{cwd}\\50_states.csv")
NUM_OF_STATES = game_data["state"].count()


#general screen settings
screen = t.Screen()
screen.title("U.S. States Game")
image = f"{cwd}\\blank_states_img.gif"
screen.addshape(image)
t.shape(image) #turtle as image background

#declare turtle that writes answers to the screen
writer = t.Turtle()
writer.penup()
writer.hideturtle()
#writer turtle constants
FONT = ("Arial", 12)
ALIGNMENT = "center"

#game loop
correct_guesses = []
score = 0
while len(correct_guesses) < NUM_OF_STATES:
    answer = screen.textinput(
        title=f"{score}/{NUM_OF_STATES} States",
        prompt="Write a state name"
    )
    answer = answer.title()
    if answer in game_data["state"].unique():
        correct_guesses.append(answer)
        answer_row = game_data[game_data.state == answer]
        xcor = int(answer_row["x"].values)
        ycor = int(answer_row["y"].values)
        writer.goto(x=xcor, y=ycor)
        writer.write(answer)
        score += 1

t.mainloop()
