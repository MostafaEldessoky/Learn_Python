# TODO: Class responsibility and main functionality 1-  2- 3- 4- ....
# TODO: Attribute ()
# ToDO: methods ()
"""
what class able to do :

how to use the class :

"""
from turtle import Turtle


class Pong(Turtle):
    def __init__(self, p, c, s="square"):
        super().__init__()
        self.penup()
        self.goto(p)
        self.shape(s)
        self.color(c)
        self.shapesize(5, 0.5)
        self.x = 0

    def up(self):
        self.x += 20
        self.sety(self.x)

    def down(self):
        self.x -= 20
        self.sety(self.x)

    def post(self):
        return self.xcor(), self.ycor()


class Text(Turtle):
    def __init__(self,p,c):
        super().__init__()
        self.color(c)
        self.penup()
        self.ht()
        self.goto(p)

    def player_score(self, x):
        self.clear()
        self.write(f"{x} ", align="center", font=('Arial', 32, 'normal'))
