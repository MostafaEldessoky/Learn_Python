from random import choice
from turtle import Turtle

food = []
for i in range(-230, 230, 20):
    for j in range(-230, 230, 20):
        food.append((i, j))


class Food_dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.r = choice(food)
        self.shapesize(.5, .5)
        self.goto(self.r)

    def eaten(self, x):
        if self.distance(x) < 15:
            self.r = choice(food)
            self.goto(self.r)
            return True
        else:
            return False
