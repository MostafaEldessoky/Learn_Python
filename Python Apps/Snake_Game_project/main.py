import Food
import Snake
import GUI

ss = Snake.Snake()
w = GUI.Window(ss.up, "Up", ss.down, "Down", ss.left_l, "Left", ss.right_r, "Right")
f = Food.Food_dot()
while True:
    w.action(.1)
    ss.move()
    ss.w()
    if f.eaten(ss.g):
        ss.eat()
    if GUI.wall(ss.g) or ss.tail_eat():
        ss.reset_snake()
        # ss.gv()
        # break
# w.stay()

