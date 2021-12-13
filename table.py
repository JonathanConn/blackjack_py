from shoe import Shoe
from player import Player
from dealer import Dealer

class Table:
    def __init__(self, playerNames=['Player']):
        self.shoe = Shoe()
        self.dealer = Dealer('Dealer')
        self.players = [Player(x) for x in playerNames]
    
    def __str__(self):               
        s = str(self.dealer)
        for p in self.players: s += str(p)
        return s


    def hit(self, p):
        p.hand.append(self.shoe.getCard())
        p.update()


    def deal(self):        
        for i in range(2):
            self.hit(self.dealer)
            for p in self.players: self.hit(p)


    def updateAll(self):
        self.dealer.updateCount()
        for p in players: p.updateCount()


    def _turnResult(self, p):
        if p.bust: print(f'{p.name} busted.')
        if p.bj: print(f'{p.name} has 21')


    def playersTurn(self):
        for p in self.players: 
            while not p.bust and not p.bj and p.option():            
                self.hit(p)            
                print(p)
            self._turnResult(p)
    
    def dealersTurn(self):
        print(f'debug {str(self.dealer)}')
        while self.dealer.count < 17:
            self.hit(self.dealer)
            print(self.dealer)
        self._turnResult(self.dealer)
    

table = Table()

table.deal()

print(table)

table.playersTurn()

table.dealersTurn()

print(table)

