import player
p1 = player.player()
p2 = player.player()
p1_cards = p1.MyCards()
p2_cards = p2.MyCards()
p1_cards = p1.MyCards()
p2_cards = p2.MyCards()
if sum(p1_cards) < 17:
    p1_cards = p1.MyCards()
if sum(p2_cards) < 17:
    p2_cards = p2.MyCards()
if (sum(p1_cards) > 21 and sum(p2_cards) > 21) or (sum(p1_cards) == sum(p2_cards)):
    print("it is a drow")
elif sum(p1_cards) > 21 :
    print("computer win")
elif sum(p2_cards) > 21 :
    print("you are the winner")
elif sum(p1_cards) > sum(p2_cards) :
    print("you are the winner")
else :
    print("computer win")
    