from cards import Card
from random import shuffle
class Shoe:
    
    def __init__(self, numOfDecks=1):
        self.deck = []

        for i in range(numOfDecks):
            for s in Card.Suite:
                for v in Card.CardValue:
                    self.deck.append(Card(s, v))

        shuffle(self.deck)

    def getCard(self):
        return self.deck.pop(0)


