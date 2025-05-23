from turtle import Turtle


class Game(Turtle):
    def __init__(self, list_data):
        super().__init__()
        self.data = list_data
        self.score = 0
        self.ht()
        self.penup()
        self.color("black")

    def wrt(self, x):
        self.goto(self.data[x][1], self.data[x][2])
        self.write(f"{self.data[x][0]}", False, "center", ('Arial', 8, 'normal'))
        self.data.pop(x)
        self.score += 1

    def user(self, y):
        for i in range(len(self.data)):
            if y == self.data[i][0].lower():
                return i
        return -1
