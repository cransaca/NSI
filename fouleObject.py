### Importations ###
from math import *

### Paramètres ###
### Fonctions ###
def signe(x):
    """Renvoie 0, -1 ou +1 selon le signe de x."""
    if x==0:
        return 0
    else:
        return x/abs(x)


### Classes ###
class Objet:
    """Un objet sur le terrain."""
    def __init__(self,boss, coord):
        self.boss=boss
        self.coord=coord

    def getCoord(self):
        """Renvoie la liste des coordonnées."""
        return self.coord


class Obstacle(Objet):
    """Un objet fixe."""
    def __init__(self,boss, coord, couleur="black"):
        Objet.__init__(self, boss, coord)
        self.couleur=couleur

class Voyageur(Objet):
    """Un objet qui bouge."""
    def __init__(self,boss, coord,destination, couleur="black"):
        Objet.__init__(self, boss, coord)
        self.couleur=couleur
        self.destination=destination

        self.vitesse=[0,0]

    def definirVitesse(self):
        """Définie la direction à prendre."""
        None






    def avancer(self):
        None

    def testFin(self):
        """Teste si le voyageur est arrivé."""
        if self.coord==self.destination:
            return True
        else:
            return False













