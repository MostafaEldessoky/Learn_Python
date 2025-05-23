import random
class player:
    def __init__(self): 
        self.mine = []
        
    def MyCards(self):
        self.mine.append(random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))
        return self.mine
            

        
        
    