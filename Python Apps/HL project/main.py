from data import data
import random

score = 1
x1 = random.choice(data)
data.remove(x1)
x2 = random.choice(data)
data.remove(x2)
while score != 0:
    
    if len(data) == 0:
        break
    while True:
        y = input(f"what the has more follower than the other {x1['name']} that is {x1['description']} in {x1['country']} country or {x2['name']} that is {x2['description']} in {x2['country']} country type 1 for first and 0 for other  ")
        
        if (y == '0' and x1['follower_count'] < x2['follower_count']):
            print(f"well done your score is {score}")
            score = score + 1
            x1 = random.choice(data)
            data.remove(x1)
            break
        elif (y == '1' and x1['follower_count'] > x2['follower_count'] ):
            print(f"well done your score is {score}")
            score = score + 1
            x2 = random.choice(data)
            data.remove(x2)
            break
        elif (y == '0' and x1['follower_count'] > x2['follower_count'] ) or (y == '1' and x1['follower_count'] < x2['follower_count']):
            print(f"ooh no game over your last score is {score-1}")
            score = 0
            break
        else :
            print("pls enter valed input")