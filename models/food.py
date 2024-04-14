from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        random_posx = random.randint(-280, 280)
        random_posy = random.randint(-280, 280)
        self.goto(random_posx, random_posy)
