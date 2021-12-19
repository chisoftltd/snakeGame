import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import __main__

screen = Screen()
food = Food()
scoreboard = ScoreBoard()

screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Chisoft Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()


def game_continue():
    return screen.textinput("GAME OVER!", "Do you want to continue the game? 'y' or 'n' ").lower()


def reset():
    global screen
    global food
    global scoreboard
    global snake
    screen = Screen()
    food = Food()
    scoreboard = ScoreBoard()
    snake = Snake()
    screen.listen()
    screen.setup(width=1050, height=650)
    screen.bgcolor("black")
    screen.title("Chisoft Snake Game")
    screen.tracer(0)


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
        snake.extend()
        scoreboard.increment()

    if snake.head.xcor() > 523 or snake.head.xcor() < -523 or snake.head.ycor() > 323 or snake.head.ycor() < -323:
        if game_continue() == 'n':
            is_game_on = False
            scoreboard.game_over()
        elif game_continue() == 'y':
            screen.clear()
            reset()
            snake.create_snake()
            food.refresh()
            is_game_on = True

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            if game_continue() == 'n':
                is_game_on = False
                scoreboard.game_over()
            elif game_continue() == 'y':
                screen.clear()
                reset()
                snake.create_snake()
                food.refresh()
                is_game_on = True

screen.exitonclick()
