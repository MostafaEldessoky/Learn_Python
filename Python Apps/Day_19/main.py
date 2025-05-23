from turtle import Turtle, Screen

tim = Turtle()


def up():
    tim.forward(5)


def left():
    tim.left(10)
    tim.forward(5)


def right():
    tim.right(10)
    tim.forward(5)


def down():
    tim.backward(5)


my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=up)
my_screen.onkey(key="a", fun=left)
my_screen.onkey(key="d", fun=right)
my_screen.onkey(key="s", fun=down)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen.onkey(key="c", fun=clear)
tim.showturtle()
my_screen.exitonclick()
