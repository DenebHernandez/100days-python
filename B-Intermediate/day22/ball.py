'''Module for the ball class'''

from turtle import Turtle

MOVEMENT_DISTANCE = 5
class Ball(Turtle):
    '''Ball object class'''

    def __init__(self, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.color("grey")
        self.go_up = True
        self.go_right = True


    def move(self):
        if self.go_up:
            new_y = self.ycor() + MOVEMENT_DISTANCE
        else:
            new_y = self.ycor() - MOVEMENT_DISTANCE

        if self.go_right:
            new_x = self.xcor() + MOVEMENT_DISTANCE
        else:
            new_x = self.xcor() - MOVEMENT_DISTANCE

        self.goto(x=new_x, y=new_y)


    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.go_up = not self.go_up


    def paddle_collision(self, left_paddle: Turtle, right_paddle: Turtle):
        if self.go_right:
            distance_to_paddle = self.distance(right_paddle)
        else:
            distance_to_paddle = self.distance(left_paddle)

        if (self.xcor() > 330 or self.xcor() < -330) and distance_to_paddle <= 50:
            self.go_right = not self.go_right


    def score_point(self):
        if self.xcor() > 400:
            self.setpos(0, 0)
            self.go_right = not self.go_right
            return "l"
        elif self.xcor() < -400:
            self.setpos(0, 0)
            self.go_right = not self.go_right
            return "r"
        else:
            return ""
