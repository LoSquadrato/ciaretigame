from random import choices
from functools import reduce

from core.player import Player
from core.deck import deck_builder


def play_round(players):
    while True:
        pot = check_player(players)
        winner = check_winner(pot)
        winner.assign_score(pot)
        if not winner.hand:      
            for p in players:
                final_score_calc(p)
                print(f'{p.name} scored {p.score} points')
            break
        players = change_round(winner)
    return players

# check if player is human or bot, different behaviours for playing card
def check_player(players):
    pot = []
    try:
        for player in players:
            legit_cards = []
            print(f"\n{player.name}'s turn. Your hand:")
            for i, v in enumerate(player.hand, start=1):
                print(f'{i} -> {v}')
            if pot:
                lead_suit = pot[0].suit
                legit_cards = [c for c in player.hand if c.suit == lead_suit]
            if player.is_human:
                card = player.choose_card(pot)
                player.hand.remove(card)
                print(f'{player.name} play: {card}')
            else:
                if legit_cards:
                    card = legit_cards[0]          
                    player.hand.remove(card)
                else:
                    card = player.hand.pop(0)   
                print(f"{player.name} (BOT) plays: {card}")
            card.player = player
            pot.append(card)
            print(pot)
        return pot
    except Exception as e:
        print(f'check_player ERROR: {e}')
        return pot

def check_winner(pot):
    winner_card = pot[0]
    for c in pot:
        if c > winner_card:
                winner_card = c
    return winner_card.player

# change round order of players
def change_round(player, new_round = []):
    if player is None:
        return None
    new_round.append(player)
    if player.next == new_round[0]:
        return new_round
    print(new_round)
    return change_round(player.next, new_round)

# assign the trick bonus, empty pile stack
def final_score_calc(player):
    if not player.pile:
        player.score += 55
    player.pile.clear()
    



