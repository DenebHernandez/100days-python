'''Pong game file'''

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=user_paddle.move_up, key="w")
screen.onkeypress(fun=user_paddle.move_down, key="s")
screen.onkeypress(fun=computer_paddle.move_up, key="Up")
screen.onkeypress(fun=computer_paddle.move_down, key="Down")

time.sleep(3)
while game_is_on:
    screen.update()
    ball.wall_collision()
    ball.paddle_collision(right_paddle=computer_paddle, left_paddle=user_paddle)
    scoreboard.update_score(ball.score_point())
    ball.move()
    time.sleep(0.02)

screen.exitonclick()
