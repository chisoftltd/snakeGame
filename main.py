from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Chisoft Snake Game")

for turtle_index in range(3):
    crazy = Turtle()
    crazy.shape("square")
    crazy.color("white")
    crazy.goto(-(turtle_index * 20), 0)




screen.exitonclick()