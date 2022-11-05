import time
from turtle import Screen
import functions as fun
from snake_structure import segments

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

game_is_on = True

screen.listen()
screen.onkey(fun=fun.heading_north, key="w")
screen.onkey(fun=fun.heading_south, key="s")
screen.onkey(fun=fun.heading_east, key="d")
screen.onkey(fun=fun.heading_west, key="a")

while game_is_on:
    screen.update()
    new_cordinates = segments[0].pos()
    segments[0].forward(20)
    time.sleep(0.1)
    for segment in segments[1:]:
        old_cordinates = segment.pos()
        segment.setpos(new_cordinates)
        new_cordinates = old_cordinates
        # time.sleep(0.1)

screen.exitonclick()
