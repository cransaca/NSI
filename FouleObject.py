### Importations ###
#from math import *

### Paramètres ###
### Fonctions ###
def signe(x):
    """Renvoie 0, -1 ou +1 selon le signe de x."""
    if x==0:
        return 0
    else:
        return int(x/abs(x))

def addListe(l1,l2):
    """Additionne les valeurs de deux listes de même taille."""
    if len(l1)==len(l2):
        l3=[]
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
        return l3
    else:
        return []

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
    def __init__(self,boss, coord,destination,couleur="black"):
        Objet.__init__(self, boss, coord)
        self.couleur=couleur
        self.destination=destination
        self.direction=(0,0)
        self.directionPossible=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        self.objetProche={} # Dictionnaire des cases autour

    def regarderAutour(self):
        """Actualise la liste objets autour du voyageur."""
        # Réinitialise le tableau des objets proches
        self.objetProche={}
        for i in range(-1,2):
            for j in range(-1,2):
                self.objetProche[i,j]=None
        # Recherche des objets proches
        for obj in self.boss.getObjects():
            X=obj.coord[0]-self.coord[0]
            Y=obj.coord[1]-self.coord[1]
            if -1<=X<=1 and -1<=Y<=1:
                self.objetProche[X,Y]=obj

    def definirVitesse(self):
        """Définie la direction à prendre."""
        self.direction=(signe(self.destination[0]-self.coord[0]),signe(self.destination[1]-self.coord[1]))
        self.regarderAutour()

        # Si la case n'est pas libre
        if self.objetProche[self.direction]!=None and not self.testFin():
            # On test les autres directions
            i=self.directionPossible.index(self.direction)
            if self.objetProche[self.directionPossible[(i+1)%8]]==None:
                self.direction=self.directionPossible[(i+1)%8]
            elif self.objetProche[self.directionPossible[(i-1)%8]]==None:
                self.direction=self.directionPossible[(i-1)%8]
            elif self.objetProche[self.directionPossible[(i+2)%8]]==None:
                self.direction=self.directionPossible[(i+2)%8]
            elif self.objetProche[self.directionPossible[(i-2)%8]]==None:
                self.direction=self.directionPossible[(i-2)%8]
            else:
                self.direction=(0,0)

    def avancer(self):
        """Avance le voyageur dans la direction défini par vitesse."""
        self.definirVitesse()
        self.coord=addListe(self.coord,self.direction)

    def testFin(self):
        """Teste si le voyageur est arrivé."""
        if self.coord==self.destination:
            return True
        else:
            return False






if __name__=="__main":
    pass





