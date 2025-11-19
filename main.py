import os 
import sys

from core.player import *
from core.game import *
from core.card import *


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            with open('help.txt') as f:
                help_text = f.read()
                print(help_text)
    else:
        try:
            gioca_partita()
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(1)


def gioca_partita():
    game = GiocoCarte(['Nicola', 'Ilenia', 'Valentina', 'Bano'])
    
    print("=" * 50)
    print("INIZIO PARTITA")
    print("=" * 50)

    game.distribuisci_carte()
    
    primo_giocatore = 0
    
    # Gioca 10 mani (10 carte per giocatore)
    for mano_num in range(10):
        print(f"\n{'='*50}")
        print(f"MANO {mano_num + 1}/10")
        print(f"{'='*50}")
        # Il vincitore della mano inizia la mano successiva
        primo_giocatore = game.gioca_mano(primo_giocatore)
    
    # Calcola risultati finali
    game.calcola_vincitore()
            

if __name__ == "__main__":
    main()
