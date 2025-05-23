from random import choice, shuffle
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

rand_list = []
for i in range(-230, 231, 15):
    rand_list.append(i)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 1)
        self.penup()
        self.x = 0

    def creation(self):
        self.color(choice(COLORS))
        shuffle(rand_list)
        self.goto(290, choice(rand_list))

    def move(self):
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE + self.x)
