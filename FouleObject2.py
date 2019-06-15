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

### Classes ###
class Observable:
    def __init__(self, vue):
        self.observateurs = []

    def attacher_observateur(self, observateur):
        self.observateurs.append(observateur)

    def notifier(self):
         #print("On notifie",len(self.observateurs))
        for o in self.observateurs:# pas besoin de boucle
            o.mise_a_jour(self)


class Objet(Observable):
    """Un objet sur le terrain."""
    def __init__(self,boss, coord):
        Observable.__init__(self,boss)
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


    def avancer(self):
        """Définie la direction à prendre."""
        x1,y1=self.coord[0], self.coord[1]
        self.direction=(signe(self.destination[0]-x1),signe(self.destination[1]-y1))
        x=self.direction[0]
        y=self.direction[1]
        listDirections=[(x1+x,y1+y),(x1+signe(x+y),y1+signe(-x+y)),(x1+signe(x-y),y1+signe(x+y)),(x1-y,y1+x),(x1+y,y1-x)]

        # Recherche des objets proches
        for obj in self.boss.getObjects():
            o=obj.getCoord()
            if o in listDirections:
                listDirections.remove(o)
                #définition de la nouvelle direction
        if  listDirections==[]:
            self.coord=(0,0)
        else:
            self.coord=listDirections[0]

          #print("On avance2",self.coord,self.direction)
        self.notifier()


    def testFin(self):
        """Teste si le voyageur est arrivé."""
        if self.coord==self.destination:
            return True
        else:
            return False






if __name__=="__main":
    pass

