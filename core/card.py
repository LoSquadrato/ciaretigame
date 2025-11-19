from enum import Enum

class Seme(Enum):
    CUORI = "♥"
    QUADRI = "♦"
    FIORI = "♣"
    PICCHE = "♠"

class Card:

    def __init__(self, valore, seme):
        self.valore = valore
        self.seme = seme
        self.possesso = None

    def __str__(self):
        return f"{self.valore}{self.seme.value}"
    
    def __repr__(self):
        return self.__str__()

