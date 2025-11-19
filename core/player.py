import random

class Giocatore:
         
    def __init__(self, nome):
        self.nome = nome
        self.is_umano = False
        self.mano = []
        self.carte_prese = []
        

    def ricevi_carta(self, carta):
        self.mano.append(carta)
    
    def ha_seme(self, seme):
        return any(carta.seme == seme for carta in self.mano)
    
    def gioca_carta(self, index):
        return self.mano.pop(index)
    
    def carte_giocabili(self, seme_obbligatorio):
        if seme_obbligatorio is None:
            return list(range(len(self.mano)))
        if self.ha_seme(seme_obbligatorio):
            return [i for i, carta in enumerate(self.mano) 
                    if carta.seme == seme_obbligatorio]
        return list(range(len(self.mano)))
    
    def calcola_punti(self, seme_da_punti):
        return sum(carta.valore for carta in self.carte_prese if carta.seme == seme_da_punti)
    
    def __str__(self):
        return f"{self.nome}: {self.mano}"


