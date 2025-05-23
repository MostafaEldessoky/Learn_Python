from turtle import Turtle

up = 90
down = 270
right = 0
left = 180
ss = Turtle()


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_list = []
        self.score = 0
        self.creation()
        self.g = self.snake_list[0].position()
        self.gg = self.snake_list[-1].position()
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())

    def creation(self, segment=3):
        for i in range(segment):
            self.segment((i * -20, 0))

    def segment(self, p):
        s = Turtle("square")
        s.color("red")
        s.penup()
        s.speed("fastest")
        s.shapesize(1, 1)
        s.goto(p)
        self.snake_list.append(s)

    def move(self):
        for i in range(len(self.snake_list) - 1):
            self.snake_list[len(self.snake_list) - 1 - i].goto(self.snake_list[len(self.snake_list) - 2 - i].position())
        self.snake_list[0].forward(20)
        self.g = self.snake_list[0].position()
        self.gg = self.snake_list[-1].position()

    def tail_eat(self):
        for i in range(1, len(self.snake_list)):
            if self.snake_list[i].distance(self.g) < 15:
                return True
        else:
            return False

    def eat(self):
        self.segment(self.gg)
        self.score += 1

    def up(self):
        if self.snake_list[0].heading() != down:
            self.snake_list[0].setheading(up)

    def left_l(self):
        if self.snake_list[0].heading() != right:
            self.snake_list[0].setheading(left)

    def right_r(self):
        if self.snake_list[0].heading() != left:
            self.snake_list[0].setheading(right)

    def down(self):
        if self.snake_list[0].heading() != up:
            self.snake_list[0].setheading(down)

    def w(self):
        ss.reset()
        ss.ht()
        ss.penup()
        ss.goto(0, 260)
        ss.color("green")
        ss.write(arg=f"score : {self.score}  high score : {self.high_score}", move=False, align='center',
                 font=('Arial', 18, 'normal'))

    def reset_snake(self):
        self.snake_list[0].goto(0, 0)
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0

    # def gv(self):
    #     ss.ht()
    #     ss.penup()
    #     ss.goto(0, 0)
    #     ss.color("green")
    #     ss.write(arg=f"Game Over", move=False, align='center', font=('Arial', 20, 'normal'))
