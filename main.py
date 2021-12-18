import time
from turtle import Turtle, Screen
from snake import Snake
import random

screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Chisoft Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
