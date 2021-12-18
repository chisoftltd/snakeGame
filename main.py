import time
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
    screen.update()
    time.sleep(0.1)
    for turtle_num in range(len(turtle_list) - 1, 0, -1):
        new_x = turtle_list[turtle_num - 1].xcor()
        new_y = turtle_list[turtle_num - 1].ycor()
        turtle_list[turtle_num].goto(new_x, new_y)
    turtle_list[0].forward(20)
    #turtle_list[0].left(90)
screen.exitonclick()
