import random

from core.player import *
from core.card import *
from core.valid_input import *

class GiocoCarte:
    def __init__(self, nomi_giocatori):
        if nomi_giocatori is None:
            nomi_giocatori = [f"Giocatore {i+1}" for i in range(4)]
        
        self.giocatori = [Giocatore(nome) for nome in nomi_giocatori]
        self.mazzo: List[Carta] = []
        self.turno_corrente = 0
        self.inizializza_mazzo()
    
    def inizializza_mazzo(self):
        # Crea il mazzo
        self.mazzo = [Card(valore, seme) for seme in Seme for valore in range(1, 11)]
        random.shuffle(self.mazzo)
    
    def distribuisci_carte(self):
        # Distribuisce 10 carte a ciascun giocatore
        for i, carta in enumerate(self.mazzo):
            self.giocatori[i % 4].ricevi_carta(carta)
        print("=== CARTE DISTRIBUITE ===")
        for giocatore in self.giocatori:
            print(f"{giocatore.nome}: {sorted(giocatore.mano, key=lambda c: (c.seme.name, c.valore))}")
        print()
    
    def gioca_mano(self, primo_giocatore_idx):
        carte_giocate = []  # (indice_giocatore, carta)
        seme_primo = None
        
        print(f"\n--- Inizia la mano: {self.giocatori[primo_giocatore_idx].nome} ---")
        
        for i in range(4):
            idx_giocatore = (primo_giocatore_idx + i) % 4
            giocatore = self.giocatori[idx_giocatore]
            
            # Determina carte giocabili
            carte_giocabili = giocatore.carte_giocabili(seme_primo)
            
            print(f"\n{giocatore.nome} - Mano: {giocatore.mano}")
            print(f"Carte giocabili: {[giocatore.mano[i] for i in carte_giocabili]}")
            
            # Opzione is_umano per prossima implematazione
            if giocatore.is_umano:
                indice_scelto = input_selezione_carta()
            else:
                indice_scelto = carte_giocabili[0]

            carta_giocata = giocatore.gioca_carta(indice_scelto)
            
            print(f">>> {giocatore.nome} gioca: {carta_giocata}")
            
            if seme_primo is None:
                seme_primo = carta_giocata.seme
                print(f"Seme di mano: {seme_primo.value}")
            
            carte_giocate.append((idx_giocatore, carta_giocata))
        
        # Determina vincitore: carta più alta del seme di mano
        vincitore_idx, carta_vincente = max(
            [(idx, carta) for idx, carta in carte_giocate if carta.seme == seme_primo],
            key=lambda x: x[1].valore
        )
        
        # Il vincitore prende tutte le carte
        vincitore = self.giocatori[vincitore_idx]
        for _, carta in carte_giocate:
            vincitore.carte_prese.append(carta)
        
        print(f"\n🏆 {vincitore.nome} vince la mano con {carta_vincente}!")
        print(f"Carte prese: {[c for _, c in carte_giocate]}")
        
        return vincitore_idx
    
    def calcola_vincitore(self):
                
        print("\n" + "=" * 50)
        print("RISULTATI FINALI")
        print("=" * 50)
                
        risultati = {}
                
        for giocatore in self.giocatori:
            print(f"\n{giocatore.nome} - Carte prese: {len(giocatore.carte_prese)}")
                    
            # Se non ha preso nessuna mano, assegna 55 punti
            if len(giocatore.carte_prese) == 0:
                risultati[giocatore.nome] = (55, None)
                print(f"  ⚠️  Nessuna mano presa → 55 punti di penalità")
                continue
            # Calcola punti carte di cuori pescate
                    
            punti = giocatore.calcola_punti(Seme.CUORI)
            print(f"  Hai ottenuto: {punti} punti")               
            risultati[giocatore.nome] = (punti)
                    
                
                # Determina vincitore
        vincitore = min(risultati.items(), key=lambda x: x[0])
                
        print("\n" + "🎉" * 25)
        if vincitore[1][1] is None:
            print(f"VINCITORE: {vincitore[0]} con {vincitore[1][0]} punti")
        else:
            print(f"VINCITORE: {vincitore[0]} con {vincitore[1][0]} punti ({vincitore[1][1].value})!")
        print("🎉" * 25)

