'''snake game file'''
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.reposition()
        scoreboard.update_score()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

# scoreboard.game_over()
scoreboard.reset()

screen.exitonclick()
