import random

from core.valid_input import *
from core.costants import BOT_NAME, SUIT



class Player:
         
    def __init__(self, name, is_human):
        self.name = name
        self.hand = []
        self.score = 0
        self.is_human = is_human
        self.pile = []
        self.next = None

    def __repr__(self):
        if self.is_human:
            return f'{self.name}'
        return f'{self.name} (BOT)'

    # method that assign the next turn player
    def is_next(self, lst):
        if len(lst) == 3:
            self.next = lst[0]
        if lst: 
            lst[-1].next = self   
        return self

    # metod for human players for choose card with the correct input
    def choose_card(self, pot):      
        print(f'{self.name} choose your card:')
        card = valid_input_card(self.hand)
        return card

    # metod for assign card's point to player who win the round
    def assign_score(self, pot):
        for c in pot:
            if c.suit == 'Coins':
                self.score += c.value
        print(f'{self.name} have {self.score} point')
        self.pile.extend(pot)
    
# init players and append in the players list    
def players_in_game():
    players = []
    # implemented only for 4 players
    for i in range(4):
        is_human = conf_input('This player is a person?\n y/N\n')
        if is_human:
            name_player = valid_input_name()
            print(f'Human player {name_player} entered the game')
        else:
            name_player = BOT_NAME[i]
            print(f'BOT player {name_player} entered the game')
        player = (Player(name_player, is_human)).is_next(players)
        players.append(player)

    return players



