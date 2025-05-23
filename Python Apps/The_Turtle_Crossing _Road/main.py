import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen definition
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
# level score screen definition
s = Scoreboard()
# player definition
p = Player()

# cars definition
car_list = []


def car_generator(z):
    c = CarManager()
    c.creation()
    c.x += z
    car_list.append(c)


# control definition
screen.listen()
screen.onkey(p.up, "Up")

i = 1
h = 0
n = 11
m = n - 1
on_game = True
while on_game:
    time.sleep(0.1)
    screen.update()
    m += 1
    if m % n == 0:
        car_generator(h)
    for j in range(len(car_list)):
        car_list[j].move()
    s.level(i)
    if p.is_level():
        n -= 1
        i += 1
        h += 10
        p.creation()
    if n == 0:
        s.win()
        on_game = False
    for d in range(len(car_list)):
        if p.is_collision(car_list[d].position()):
            s.game_over()
            on_game = False
            break

screen.exitonclick()
