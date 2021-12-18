from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for turtle_index in range(3):
            crazy = Turtle("square")
            crazy.penup()
            crazy.color("white")
            crazy.goto(-(turtle_index * 20), 0)
            self.turtle_list.append(crazy)

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_num - 1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)
        self.turtle_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
