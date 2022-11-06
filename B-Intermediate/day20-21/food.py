'''Module for food object'''

import random
from turtle import Turtle

NEGATIVE_EDGE = -280
POSITIVE_EDGE = 280


class Food(Turtle):
    '''Class for food objects'''

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.goto(
            x=random.randint(NEGATIVE_EDGE, POSITIVE_EDGE),
            y=random.randint(NEGATIVE_EDGE, POSITIVE_EDGE)
        )


    def reposition(self):
        '''Repositions food to a random position on the board'''
        self.goto(
            x=random.randint(NEGATIVE_EDGE, POSITIVE_EDGE),
            y=random.randint(NEGATIVE_EDGE, POSITIVE_EDGE)
       )
