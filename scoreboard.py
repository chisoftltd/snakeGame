from turtle import Turtle

# from food import Food


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()

    def displayscore(self, score):
        self.goto(0, 300)
        self.color("white")
        self.clear()
        self.write(f"Score: {score}", move=True, align="center", font=("Verdana", 15, "normal"))
