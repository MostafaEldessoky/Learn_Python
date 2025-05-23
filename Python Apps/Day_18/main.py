import turtle
from random import choice, randint

tim = turtle.Turtle()
tim.shape("arrow")
x = ["Red", "Blue", "Lime", "DeepPink", 'Gold', "Gainsboro", "Green", "Cyan", "DeepSkyBlue", "Coral", "LightCoral",
     "Indigo", "BlueViolet", "MediumVioletRed"]

# for _ in range(1000):
#     y = randint(0, 3)
#     tim.color(choice(x))
#     tim.speed("fastest")
#     tim.pensize(10)
#     if y == 0:
#         tim.forward(30)
#     elif y == 1:
#         tim.left(90)
#         tim.forward(30)
#     elif y == 2:
#         tim.right(90)
#         tim.forward(30)
#     elif y == 3:
#         tim.backward(30)
for _ in range(0, 361):
    for i in range(0,101):
        tim.color(choice(x))
        tim.speed("fastest")
        tim.circle(i)
        tim.right(1)
screen = turtle.Screen()
screen.exitonclick()
