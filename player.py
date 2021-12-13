from cards import Card

class Player():
    def __init__(self, name='NoName'):
        self.hand = []
        self.name = name
        
        self.count = 0
        self.bust = False
        self.bj = False

    def __str__(self):
        return f'{self.name} {self.hand} = {self.count}\n'

    def update(self):
        total = 0
        for c in self.hand:
            if c.getVal() == Card.CardValue.ACE:
                if total + 11 > 21:
                    total += 1
            else:
                total += c.getVal()        
        self.count = total
        self.bust = True if self.count > 21 else False
        self.bj = True if self.count == 21 else False

    # option to hit or stay
    def option(self):
        opt = input(f'{self.name} Hit? (y): ')
        return True if opt == 'y' else False 


    
