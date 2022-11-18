'''Module for snake object class'''

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Creates a snake with starting lenght of three segments'''

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) -1]


    def create_snake(self):
        '''Adds the initial three segments to the snake body'''

        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        '''Creates snakes segments at the required position'''

        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        '''Adds a segment at the end of the snake'''

        self.add_segment(self.segments[-1].pos())


    def move(self):
        '''Function for the snakes perpetual movement forward'''

        for seg_num in range(len(self.segments) -1, 0, -1):
            new_coordinates = self.segments[seg_num -1].pos()
            self.segments[seg_num].setpos(new_coordinates)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        '''Direction control method,
        sets the snakes head heading Up'''

        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        '''Direction control method,
        sets the snakes head heading Down'''

        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        '''Direction control method,
        sets the snakes head heading Left'''

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        '''Direction control method,
        sets the snakes head heading Right'''

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for segment in self.segments:
            segment.goto(800, 800)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
