from turtle import Turtle


# from food import Food


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.displayscore(self.score)

    def displayscore(self, score):
        self.write(f"Score: {score}", move=False, align="center", font=("Verdana", 15, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.displayscore(self.score)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=("Verdana", 15, "normal"))
