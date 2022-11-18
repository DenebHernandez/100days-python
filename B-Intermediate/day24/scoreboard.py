'''Module for the scoreboard class'''

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15)

class Scoreboard(Turtle):
    '''Turtle objects that tracks the user score and
    displays it at the top of the screen'''

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(270)
        self.update_scoreboard()


    def update_scoreboard(self):
        '''Rewrites the score onto the screens'''
        self.clear()
        self.write(
            arg=f"Score =  {self.score}  High score = {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     '''Writes a game over message to the center of the screen'''

    #     self.goto(0, 0)
    #     self.write(
    #         arg="GAME OVER",
    #         align=ALIGNMENT,
    #         font=FONT
    #     )


    def update_score(self):
        '''Increases score by one'''

        self.score += 1
        self.update_scoreboard()
