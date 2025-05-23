from turtle import Turtle, Screen
from random import randint

s = Screen()
s.setup(500, 400)
u = s.textinput(title="make your bet", prompt="which turtle will win the race enter color ")
if u == "red":
    u = 0
elif u == "blue":
    u = 1
elif u == "green":
    u = 2
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t1.color("red")
t2.color("blue")
t3.color("green")
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t1.penup()
t2.penup()
t3.penup()
t1.goto(-230, -150)
t2.goto(-230, 0)
t3.goto(-230, 150)
while True:
    if t1.xcor() < 230 or t1.xcor() < 230 or t1.xcor() < 230:
        r = randint(1, 20)
        t1.forward(r)
        r = randint(1, 20)
        t2.forward(r)
        r = randint(1, 20)
        t3.forward(r)
    else:
        q = [t1.xcor(), t2.xcor(), t3.xcor()]
        y = max([t1.xcor(), t2.xcor(), t3.xcor()])
        q1 = q.index(y)
        if q1 == u:
            print("yes you got it ")
        else:
            print("sorry you lose")
        break

s.exitonclick()
