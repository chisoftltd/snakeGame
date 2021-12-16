from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Chisoft Snake Game")
screen.tracer(0)

turtle_list = []
directions = [0, 90, 180, 270]
speed = [10, 20, 30, 40, 50]

for turtle_index in range(3):
    crazy = Turtle(shape="square")
    crazy.penup()
    crazy.color("white")
    crazy.goto(-(turtle_index * 20), 0)
    turtle_list.append(crazy)

screen.update()

is_game_on = True
while is_game_on:
    for turtle in turtle_list:
        turtle.forward(20)
        turtle.right(90)


screen.exitonclick()
