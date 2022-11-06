'''Module for the ball class'''

from turtle import Turtle

class Ball(Turtle):
    '''Ball object class'''

    def __init__(self, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.color("grey")
