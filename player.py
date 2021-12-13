from cards import Card
class Player():
    def __init__(self, name='bob'):
        self.hand = []
        self.name = name
        self.count = 0
   
    def __str__(self):
        return f'{slef.name} {self.hand} = {self.count}'

    def updateCount(self):
        total = 0
        for c in self.hand:
            if c.getVal() == Card.CardValue.ACE:
                if total + 11 > 21:
                    total += 1
            else:
                total += c.getVal()        
        self.count = total



