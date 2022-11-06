'''Pong game file'''

# import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

LEFT_PADDLE_POS = (-350, 0)
RIGHT_PADDLE_POS = (350, 0)

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")

user_paddle = Paddle(paddle_pos=LEFT_PADDLE_POS)
computer_paddle = Paddle(paddle_pos=RIGHT_PADDLE_POS)
ball = Ball()

screen.listen()
screen.onkeypress(fun=user_paddle.move_up, key="Up")
screen.onkeypress(fun=user_paddle.move_down, key="Down")

while game_is_on:
    screen.update()

screen.exitonclick()
