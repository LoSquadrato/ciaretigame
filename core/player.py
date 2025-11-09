from core.valid_input import *
from core.costants import BOT_NAME, SUIT

import random

class Player:
         
    def __init__(self, name, is_human):
        self.name = name
        self.hand = {}
        self.score = 0
        self.is_human = is_human
        self.taken = []

    def remove_card(self, card):
        new_hand = {}
        for k, c in self.hand.items():
            if c != card:
                new_hand[len(new_hand) + 1] = c
        self.hand = new_hand
    

    def ins_card(self,card):
        self.hand[len(self.hand) + 1] = card


    def choose_card(self, pot):
        print(f"\n{self.name}'s turn. Your hand:")
        # implemantare il caso che un giocatore non abbia carte valide
        for k, card in self.hand.items():
            print(f'{k} -> {card}')
        if len(pot)>0:
            lead_suit = pot[0].suit
            for card in self.hand.values():
                card.is_legit = (card.suit == lead_suit)
        print(f'{self.name} choose your card:')
        card = valid_input_card(self.hand)
        print(f'{self.name} play: {card}')
        return card

    def empty_pot(self, pot):
        for c in pot:
            c.player = self.name
            if c.suit == SUIT[0]:
                self.score += c.value
        self.taken.extend(pot)
        pot.clear()

       
def players_in_game():
    players = []
    for i in range(4):
        is_human = conf_input('This player is a person?\n y/N\n')
        if is_human:
            name_player = valid_input_name()
            print(f'Human player {name_player} entered the game')
        else:
            name_player = random.choice(BOT_NAME)
            print(f'BOT player {name_player} entered the game')
        players.append(Player(name_player, is_human))
        
    return players

def check_player(players):
    pot = []
    try:
        for player in players:
            if player.is_human == True:
                card = player.choose_card(pot)
            else:
                card_key = next(iter(player.hand))
                card = player.hand.pop(card_key)
                print(f"{player.name} (BOT) plays: {card}")
            card.player = player.name
            pot.append(card)
        return pot
    except Exception as e:
        print(f'check_player ERROR: {e}')
        return []

def check_winner(pot):
    if not pot:
        return None
    winner_card = pot[0]
    for c in pot[1:]:
        if c.suit == winner_card.suit and c.value > winner_card.value:
                winner_card = c
    return winner_card.player
