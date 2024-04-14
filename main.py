import time
from turtle import Screen

from models.food import Food
from models.snake import Snake
from models.score import Score


def commands(tommy):
    from turtle import Screen
    screen = Screen()
    screen.listen()
    screen.onkey(tommy.go_up, "Up")
    screen.onkey(tommy.go_right, "Right")
    screen.onkey(tommy.go_left, "Left")
    screen.onkey(tommy.go_down, "Down")


def screen_setup():
    from turtle import Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)


def main():
    screen_setup()
    screen = Screen()
    tommy = Snake()
    apple = Food()
    commands(tommy)
    score = Score()

    # Game loop
    game_is_running = True
    while game_is_running:
        screen.update()
        time.sleep(0.1)
        tommy.snake_infinite_moving()
        if tommy.head.distance(apple) < 15:
            apple.refresh_food()
            tommy.extend_snake()
            score.score_count()

        if tommy.head.xcor() > 290 or tommy.head.xcor() < -290 or tommy.head.ycor() > 290 or tommy.head.ycor() < -290:
            score.game_over()
            game_is_running = False

        for segment in tommy.full_snake:
            if tommy.head.distance(segment) < 10 and segment == tommy.full_snake[1:]:
                score.game_over()
                game_is_running = False

    # Close the screen when clicked
    screen.exitonclick()


if __name__ == '__main__':
    main()
