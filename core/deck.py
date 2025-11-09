from core.costants import SUIT
from core.player import Player
import random

class Card:

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        self.player = ''
        self.is_legit = True

    def __repr__(self):
        return f'{self.value} of {self.suit}'

def deck_builder(suit):
    deck = []
    for s in suit:
        for v in range(1, 11):
            card = Card(s, v)
            deck.append(card)
    return deck

def initial_hand(players):
        deck = deck_builder(SUIT)
        random.shuffle(deck)
        while len(deck)>0:
            for p in players:
                card = deck.pop()
                card.player = p.name
                p.ins_card(card)
        print(f'Every players received {len(players[0].hand)} cards')

            