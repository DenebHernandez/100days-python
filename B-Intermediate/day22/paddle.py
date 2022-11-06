'''Module for the paddle object'''

from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    '''Paddle object that of lenght 5'''

    def __init__(self, paddle_pos):
        super().__init__(shape="square")
        self.penup()
        self.setpos(paddle_pos)
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)


    def move(self, y_pos):
        '''Moves the paddle to the y position passed on the argument'''
        self.setpos(x=self.xcor(), y=y_pos)


    def move_up(self):
        ''''Moves the paddle up a constant distance'''
        y_pos = self.ycor() + MOVE_DISTANCE
        self.move(y_pos=y_pos)


    def move_down(self):
        '''Moves the paddle down a constant distance'''
        y_pos = self.ycor() - MOVE_DISTANCE
        self.move(y_pos=y_pos)
