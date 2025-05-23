import turtle
import pandas as pd
from States_Names import Game

data = pd.read_csv("50_states.csv")
dic_data = data.to_dict()
list_data = [(dic_data["state"][i], dic_data["x"][i], dic_data["y"][i]) for i in range(len(dic_data["x"]))]

screen = turtle.Screen()
screen.setup(735, 520)
screen.bgcolor("black")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.title("U.S. States Game")

g = Game(list_data)

while True:
    if g.score != 50:
        inp = screen.textinput(title=f"{g.score}/50 State Correct", prompt="What is another state name?").lower()
        a = g.user(inp)
        if a != -1:
            g.wrt(a)
    else:
        break
screen.exitonclick()












