from shoe import Shoe
from player import Player
from dealer import Dealer

class Table:
    def __init__(self, numOfPlayers=1):
        self.shoe = Shoe()
        self.dealer = Dealer()
        self.players = [Player()] * numOfPlayers
    
    def __str__(self):               
        s = f'Dealer {self.dealer.hand} -> {self.dealer.getCount()}\n'

        for p in self.players: s += p

        return s

    def hit(self, player):
        player.hand.append(self.shoe.getCard())

    def deal(self):        
        for i in range(2):
            self.hit(self.dealer)

            for p in self.players:
                self.hit(p)
   
    def determineWinner(self):
        
        dealerCount = self.dealer.getCount()

        for p in self.players:
            playerCount = p.getCount()
            
            if playerCount > 21:
                print(f'Player busts')

            elif dealerCount > 21:
                print(f'Dealer busts, player wins')

            elif playerCount == dealerCount:
                print(f'Player Pushes')

            elif playerCount > dealerCount:
                print(f'Player Wins')

            else:
                print(f'Dealer Wins')

table = Table()

table.deal()
print(table)

table.playersTurn()
table.dealersTurn()

table.determineWinner()


