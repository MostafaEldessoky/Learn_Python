# TODO: create class C1 for the main functionality of the players objects ( 2 objects will be created from this class)
# TODO: create class C2 that inheritance form C1 to be able to track score and pass it to the screen ( 2 objects will be created from this class)
# TODO: create class c3 that inheritance form c1 to make the ball functionality ( 1 object will be created)
# TODO: create the main program that use all objects to make the game work as expected
"""
what program able to do :

how to user can use the program :

"""
import turtle
from turtle import Screen
from C1 import Pong, Text
from C2 import Ping
from time import sleep

# constants:
PLAYER1_POSITION = (370, 0)
PLAYER1_COLOR = "red"
PLAYER2_POSITION = (-380, 0)
PLAYER2_COLOR = "blue"

w = Screen()
w.bgcolor("black")
w.setup(width=800, height=600)
w.title("PingXPong")
w.tracer(0)

player1 = Pong(PLAYER1_POSITION, PLAYER1_COLOR)
player2 = Pong(PLAYER2_POSITION, PLAYER2_COLOR)

ball = Ping()

t1 = Text((-200, 250), "red")
t2 = Text((200, 250), "blue")

w.listen()
w.onkey(player1.up, "Up")
w.onkey(player1.down, "Down")
w.onkey(player2.up, "w")
w.onkey(player2.down, "s")

while True:
    w.update()
    sleep(0.05)
    t1.player_score(ball.score1)
    t2.player_score(ball.score2)
    ball.ball_move()
    x1, y1 = player1.post()
    x2, y2 = player2.post()
    ball.ball_collision(x1, y1, x2, y2)
    if ball.score1 == 10 or ball.score2 == 10:
        break

w.exitonclick()
