import os 
import sys

from core.deck import initial_hand
from core.player import players_in_game
from core.game import play_round
from core.valid_input import conf_input


def game(players):
    while True:
        players = play_round(initial_hand(players))
        rep = conf_input('How about another game?\n y/N\n')
        if not rep:
            break
    print('Thank you for playing Ciareti !!!')

def main():

    print("Welcome gamer, Ciareti awaits you!!!")

    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            with open('help.txt') as f:
                help = f.read()
                print(help)

    else:
        try:
            players = players_in_game()
            game(players)   
        except Exception as e:
            print(f'ERROR! {e}')
            sys.exit(1)

    # recursively call game func till players say no

if __name__ == "__main__":
    main()
