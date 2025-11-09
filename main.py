from core.deck import initial_hand
from core.player import players_in_game
from core.round import play_round
import os 
import sys


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
            initial_hand(players)
            play_round(players)
        except Exception as e:
            print(f'ERROR! {e}')
            sys.exit(1)




if __name__ == "__main__":
    main()
