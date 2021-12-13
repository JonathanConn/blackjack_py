from player import Player

class Dealer(Player):

             
    def playersTurn(self):
        while self.dealer.getCount() < 17:
            self.hit(self.dealer)        
            print(f'Dealer {self.dealer.hand}')
    


