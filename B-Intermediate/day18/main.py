from operator import pos
from turtle import Turtle, Screen, TurtleScreen
import random
import colorgram

def random_move(turtle, color):
    turtle.pencolor(color)
    random_angle = random.randint(0, 360)
    turtle.right(random_angle)
    turtle.forward(random.randint(5, 40))

def random_color(colors):
    return random.choice(colors)

rgb_colors = []
colors = colorgram.extract("image.jpg", 10)
for color in colors:
    r = color.rgb.r
    g =color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

timmy = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
timmy.speed(0)
timmy.penup()
timmy.setpos(-250, -200)

for row in range (10):
    for column in range(11):
        timmy.dot(15, random_color(rgb_colors))
        timmy.forward(50)
    position = timmy.pos()
    timmy.setpos(-250, position[1] + 50)

# print(position)

screen.exitonclick()