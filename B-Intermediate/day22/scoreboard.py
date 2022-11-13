'''Module for the scoreboard class'''

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 17)

class Scoreboard(Turtle):
    '''Turtle objects that tracks the score and
    displays it at the top of the screen'''

    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(260)
        self.update_scoreboard()


    def update_scoreboard(self):
        '''Rewrites the score onto the screens'''

        self.write(
            arg=f"{self.left_paddle_score}   -   {self.right_paddle_score}",
            align=ALIGNMENT,
            font=FONT
        )


    # def game_over(self):
    #     '''Writes a game over message to the center of the screen'''

    #     self.goto(0, 0)
    #     self.write(
    #         arg="GAME OVER",
    #         align=ALIGNMENT,
    #         font=FONT
    #     )


    def update_score(self, paddle: str):
        '''Increases score by one'''

        if paddle == "":
            return
        elif paddle == "l":
            self.left_paddle_score += 1
        elif paddle == "r":
            self.right_paddle_score += 1

        self.clear()
        self.update_scoreboard()
