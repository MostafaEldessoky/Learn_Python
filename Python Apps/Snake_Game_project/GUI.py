from turtle import Screen
import time


def wall(q):
    if q[0] < -290.00 or q[0] > 290.00 or q[1] < -290.00 or q[1] > 290.00:
        return True
    else:
        return False


class Window:
    def __init__(self, a1, b1, a2, b2, a3, b3, a4, b4):
        self.w = Screen()
        self.w.setup(600, 600)
        self.w.bgcolor("black")
        self.w.title("my snake game")
        self.w.tracer(0)
        self.w.listen()
        self.w.onkey(a1, b1)
        self.w.onkey(a2, b2)
        self.w.onkey(a3, b3)
        self.w.onkey(a4, b4)

    def action(self, x):
        self.w.update()
        time.sleep(x)

    # def stay(self):
    #     self.w.exitonclick()
