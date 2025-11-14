import random

from core.costants import SUIT

class Card:

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        self.player = ''

    def __repr__(self):
        return f'{self.value} of {self.suit}' 

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        if self.suit == other.suit:
            return self.value > other.value 
        return False    

    # method for init player field
    def assign_card_owner(self, player):
        self.player = player.name
        return self  


# create card and popolate che deck array
def deck_builder(suit):
    deck = []
    for s in suit:
        suit_cards = [Card(s, v) for v in range(1, 11)]
        deck.extend(suit_cards)
    return deck

# draw initial hands for every players
def initial_hand(players):
    deck = deck_builder(SUIT)
    random.shuffle(deck)
    for p in players:
        cards = [deck.pop() for x in range(10)]
        p.hand.extend(cards)
    return players


            