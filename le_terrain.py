### Importations ###
from math import *
from random import *

### ParamÃƒÂ¨tres ###
### Fonctions ###
def signe(x):
    """Renvoie 0, -1 ou +1 selon le signe de x."""
    if x==0:
        return 0
    else:
        return x/abs(x)


### Importations ###
from math import *
### ParamÃ¨tres ###
### Fonctions ###

def conversionPolaireCartesien(r,theta):
    return (x,y)

def convertCartesienPolaire(x,y):
    return (r,theta)

def distance(P1,P2):
    """Renvoie la distance entre 2 points P1 et P2."""
    return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)


### Classes ###
class Observable:
    def __init__(self, vue):
        self.observateurs = []

    def attacher_observateur(self, observateur):
        self.observateurs.append(observateur)

    def notifier(self):
        for o in self.observateurs:
            o.mise_a_jour()



class Terrain():
    """Terrain dans lequel la foule se dÃ©place."""
    def __init__(self, largeur, longueur):#,obstacle=None, voyageur=None ):
        # Dimension du terrain
        self.largeur=largeur
        self.longueur=longueur

        # Organisation du terrain
        self.listAcces=[]
        self.listObstacles=[]
        self.porte=[[0,self.longueur//2],[self.largeur,self.longueur//2],[self.largeur//2,0],[self.largeur//2,self.longueur]]

        self.initObstacles()
        self.creerMurs()
        # Voyageurs
        self.listVoyageurs=[]



    def getPorte(self):
        return self.porte

    def initObstacles(self):
        self.creerObstacle([10,10])
        self.creerObstacle([30,30])
        self.creerObstacle([80,20])

    def creerObstacle(self, coord):
        """CrÃ©e un obstacle."""
        self.listObstacles.append(Obstacle(self,coord))

    def creerVoyageur(self, coord,destination):
        """CrÃ©e un nouveau voyageur."""
        self.listVoyageurs.append(Voyageur(self, coord,destination))

    def creerMurs(self):
        for i in range(self.largeur):
            if not [i,self.longueur] in self.porte:
                self.creerObstacle([i,self.longueur])
            if not [i,0] in self.porte:
                self.creerObstacle([i,0])
        for i in range(self.longueur):
            if not [i,self.longueur] in self.porte:
                self.creerObstacle([i,self.longueur])
            if not [0,i] in self.porte:
                self.creerObstacle([0,i])

    def getObjects(self):
        """Renvoie la liste des obstacles."""
        obstacles=[]
        for obst in self.listObstacles:
                obstacles.append(obst)
        for voya in self.listVoyageurs:
                obstacles.append(voya)
        return obstacles

    def avanceVoyageurs(self):
        """Fait avancer tous les voyageurs d'un cran."""
        for voya in self.listVoyageurs:
            voya.avancer()

### Classes ###
class Objet(Observable):
    """Un objet sur le terrain."""
    def __init__(self,boss, coord):
        Observable.__init__(self,boss)
        self.boss=boss
        self.coord=coord

    def getCoord(self):
        """Renvoie la liste des coordonnÃƒÂ©es."""
        return self.coord


class Obstacle(Objet):
    """Un objet fixe."""
    def __init__(self, boss, coord, couleur="black"):
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
        """DÃƒÂ©finie la direction ÃƒÂ  prendre."""
        None

    def avancer(self):
        None

    def testFin(self):
        """Teste si le voyageur est arrivÃƒÂ©."""
        if self.coord==self.destination:
            return True
        else:
            return False





terrain=Terrain(10,10)







