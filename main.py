import time
from turtle import Turtle, Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
food = Food()
scoreboard = ScoreBoard()


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

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()

    if snake.head.xcor() > 515 or snake.head.xcor() < -515 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        is_game_on = False

screen.exitonclick()
