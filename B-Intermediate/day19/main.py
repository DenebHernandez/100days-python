from turtle import Turtle, Screen
import random

is_race_on = False
winner = ''

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        current_postition = turtle.position()
        if current_postition[0] >= 230:
            is_race_on = False
            winner = turtle.color()[0]
            break

if winner == user_bet:
    print(f'You win! {winner} won the race')
else:
    print(f'You lose. The winner was {winner}')

screen.exitonclick()
