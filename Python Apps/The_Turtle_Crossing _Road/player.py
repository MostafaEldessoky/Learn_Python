from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.creation()

    def creation(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def is_level(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def is_collision(self, x):
        if self.distance(x) < 20:
            return True
        else:
            return False
