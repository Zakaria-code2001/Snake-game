from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    """
    Refining the definition of the Snake class to instantiate snake objects and endow them with movement capabilities.
    """

    def __init__(self):
        super().__init__()
        self.full_snake = []
        self.t_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.full_snake[0]
        self.direction = RIGHT
        self.locked_direction = None

    def create_snake(self):
        for position in self.t_pos:
            self.add_segment(position)

    def add_segment(self, position):
        snake_piece = Turtle("square")
        snake_piece.color("white")
        snake_piece.penup()
        snake_piece.goto(position)
        self.full_snake.append(snake_piece)

    def snake_infinite_moving(self):
        for i in range(len(self.full_snake) - 1, 0, -1):
            x = self.full_snake[i - 1].xcor()
            y = self.full_snake[i - 1].ycor()
            self.full_snake[i].goto(x, y)
        self.head.forward(MOVING_DISTANCE)

    def extend_snake(self):
        self.add_segment(self.full_snake[-1].position())

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
