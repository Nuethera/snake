from turtle import Turtle
ALIGNMENT = 'center'
FONT = "Verdana"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color("dark turquoise")
        self.user_score = 0
        self.welcome()

    def __write_score(self):
        self.write(arg=f"SCORE: {self.user_score} ", move=False, align=ALIGNMENT, font=(FONT, 20, 'normal'))

    def update_score(self):
        self.user_score += 1
        self.clear()
        self.__write_score()

    def game_over(self):
        self.clear()
        self.home()
        self.write(arg=f"GAME OVER!\nYOUR FINAL SCORE IS {self.user_score}\nPress Space to restart or\nClick anywhere to exit",
                   move=False, align=ALIGNMENT, font=(FONT, 20, 'normal'))
        self.goto(0, 270)

    def welcome(self):
        self.write(arg='Press Space key to start\nUse WASD or arrow keys to control the snake',
                   move=False, align=ALIGNMENT, font=(FONT, 14, 'normal'))

        self.goto(0, 270)
