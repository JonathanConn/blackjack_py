from random import shuffle
from enum import Enum

class Card:

    def __init__(self, suite, value):
        self.suite = suite
        self.val = value

    def __str__(self):
        return f'{self.val.value}{self.suite.value}'
    
    def __repr__(self):
        return self.__str__()

    def getVal(self):
        return self.val.value
    def getName(self):
        return self.val.name
    def getSuite(self):
        return self.suite.name

    class Suite(Enum):
        HEART = '♥'
        SPADE = '♠'
        DIAMOND = '♦'
        CLUB = '♣'

    class CardValue(Enum):
        ONE =   1
        TWO =   2
        THREE = 3
        FOUR =  4
        FIVE =  5
        SIX =   6
        SEVEN = 7
        EIGHT = 8
        NINE =  9
        TEN =   10
        JACK =  10
        QUEEN = 10
        KING =  10
        ACE =   11


