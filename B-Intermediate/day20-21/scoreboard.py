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
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(270)
        self.update_scoreboard()


    def update_scoreboard(self):
        '''Rewrites the score onto the screens'''

        self.write(
            arg=f"Score =  {self.score}",
            align=ALIGNMENT,
            font=FONT
        )


    def game_over(self):
        '''Writes a game over message to the center of the screen'''

        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            align=ALIGNMENT,
            font=FONT
        )


    def update_score(self):
        '''Increases score by one'''

        self.score += 1
        self.clear()
        self.update_scoreboard()
