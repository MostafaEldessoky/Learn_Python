###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import turtle
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

timmy_my_turtle = turtle.Turtle()
timmy_my_turtle.shape("arrow")
turtle.colormode(255)
timmy_my_turtle.penup()
for j in range(-300, 10 * 40, 70):
    for i in range(-300, 10 * 40, 70):
        color = random.choice(rgb_colors)
        timmy_my_turtle.pencolor(color)
        timmy_my_turtle.setpos((i, j))
        timmy_my_turtle.dot(20)

screen = turtle.Screen()
screen.exitonclick()
