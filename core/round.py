from core.player import *


def play_round(players):
    pot = check_player(players)
    winner_name = check_winner(pot)
    try:    
        for p in players:
            if p.name == winner_name:
                p.empty_pot(pot)
                if len(p.hand) == 0:
                    for p in players:
                        print(f'{p.name} have scored {p.score} point')
                    return 
                change_round(p, players)
                break
            continue
    except Exception as e:
        print(f'round ERROR: {e}')
    play_round(players)    

   
# il giocatore che ha vinto inizia il turno successivo
def change_round(player, players):
    return players


