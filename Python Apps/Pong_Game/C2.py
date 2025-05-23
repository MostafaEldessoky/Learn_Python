# TODO: Class responsibility and main functionality 1-  2- 3- 4- ....
# TODO: Attribute ()
# ToDO: methods ()
"""
what class able to do :

how to use the class :

"""

from turtle import Turtle
from random import choice


class Ping(Turtle):
    def __init__(self):
        self.creation()
        self.score1 = 0
        self.score2 = 0

    def creation(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.x = choice([-10, 10])
        self.y = choice([-10, 10])

    def ball_move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def ball_collision(self, p1x, p1y, p2x, p2y):
        if self.ycor() < -260 or self.ycor() > 260:
            self.y *= -1.1
        elif (self.xcor() > p1x - 10 and p1y + 50 > self.ycor() > p1y - 50) or (
                self.xcor() < p2x + 10 and p2y + 50 > self.ycor() > p2y - 50):
            self.x *= -1.1
        elif self.xcor() > 410:
            self.score2 += 1
            self.creation()
        elif self.xcor() < -410:
            self.score1 += 1
            self.creation()
