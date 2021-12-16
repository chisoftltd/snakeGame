from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Chisoft Snake Game")
turtle_list = []
directions = [0, 90, 180, 270]
speed = [10, 20, 30, 40, 50]



for turtle_index in range(3):
    crazy = Turtle()
    crazy.penup()
    crazy.shape("square")
    crazy.color("white")
    crazy.goto(-(turtle_index * 20), 0)
    crazy.forward(random.choice(speed))
    crazy.setheading(random.choice(directions))
    turtle_list.append(crazy)


for turtle in turtle_list:
    turtle.forward(random.choice(speed))
    turtle.setheading(random.choice(directions))







screen.exitonclick()