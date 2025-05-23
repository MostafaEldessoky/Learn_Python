from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()

    def level(self, x):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {x}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)

    def win(self):
        self.goto(0, 0)
        self.write(f"YOU WON", False, "center", FONT)
