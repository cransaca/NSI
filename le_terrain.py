# coding: utf-8
### Importations ###
from math import *
from random import *
from FouleObject2 import *
### Paramètres ###
### Fonctions ###
def signe(x):
    """Renvoie 0, -1 ou +1 selon le signe de x."""
    if x==0:
        return 0
    else:
        return x/abs(x)


### Importations ###
from math import *
### Paramètres ###
### Fonctions ###

def conversionPolaireCartesien(r,theta):
    return (x,y)

def convertCartesienPolaire(x,y):
    return (r,theta)

def distance(P1,P2):
    """Renvoie la distance entre 2 points P1 et P2."""
    return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)
def dist(P1,P2):
    """Renvoie la distance entre 2 points P1 et P2."""
    (a,b)=P1
    (c,d)=P2
    return sqrt((a-c)**2+(b-d)**2)



### Classes ###

class Terrain():
    """Terrain dans lequel la foule se dÃ©place."""
    def __init__(self, largeur, longueur):#,obstacle=None, voyageur=None ):
        # Dimension du terrain
        self.largeur=largeur
        self.longueur=longueur

        # Organisation du terrain
        self.listAcces=[]
        self.listObstacles=[]
        self.porte=[]
        self.AjouterPorte((0,self.longueur//2),5)
        self.AjouterPorte((self.largeur-1,self.longueur//2),5)
        self.AjouterPorte((self.largeur//2,0),5)
        self.AjouterPorte((self.largeur//2,self.longueur-1),5)
        #self.porte=[(0,self.longueur//2),(self.largeur-1,self.longueur//2),(self.largeur//2,0),(self.largeur//2,self.longueur-1)]
        self.creerMurs()
        self.initObstacles()
        # Voyageurs
        self.listVoyageurs=[]
        
    def AjouterPorte(self,coord,radius):
        print(coord)
        for i in range(self.largeur):
            if dist((i,self.longueur-1),coord)<radius:
                self.creerObstacle((i,self.longueur-1))
                self.porte.append((i,self.longueur-1))
            if dist((i,0),coord)<radius:
                self.creerObstacle((i,0))
                self.porte.append((i,0))
        for i in range(self.longueur):
            if dist((self.largeur-1,i),coord)<radius:
                self.creerObstacle((self.largeur-1,i))
                self.porte.append((self.largeur-1,i))
            print("point=",(0,i),"center=",coord,"dist=",dist((0,i),coord),radius)
            if dist((0,i),coord)<radius:
                self.creerObstacle((0,i))
                self.porte.append((0,i))
        print("nbporte",len(self.porte))
        print(self.porte)
    def nbPorte(self):
        return len(self.porte)

    def getPorte(self):
        return self.porte

    def initObstacles(self):
        self.creerObstacle((10,10))
        self.creerObstacle((3,3))
        for i in range(1,8):
            self.creerObstacle((i,7))



    def creerObstacle(self, coord):
        """CrÃ©e un obstacle."""
        self.listObstacles.append(Objet(self,coord))

    def creerVoyageur(self, coord,destination,couleur=(255,0,0)):
        """Crée un nouveau voyageur."""
        v=Voyageur(self, coord,destination,couleur)
        self.listVoyageurs.append(v)
    def lastVoyageur(self):
        return self.listVoyageurs[len(self.listVoyageurs)-1]

    def creerMurs(self):
        for i in range(self.largeur):
            if not (i,self.longueur-1) in self.porte:
                self.creerObstacle((i,self.longueur-1))
            if not (i,0) in self.porte:
                self.creerObstacle((i,0))
        for i in range(self.longueur):
            if not (self.largeur-1,i) in self.porte:
                self.creerObstacle((self.largeur-1,i))
            if not (0,i) in self.porte:
                self.creerObstacle((0,i))

    def getObjects(self):
        """Renvoie la liste des obstacles."""
        obstacles=[]
        for obst in self.listObstacles:
                obstacles.append(obst)
        for voya in self.listVoyageurs:
                obstacles.append(voya)
        return obstacles

    def getVoyageurs(self):
        """Renvoie la liste des obstacles."""
        obstacles=[]
        for voya in self.listVoyageurs:
                obstacles.append(voya)
        return obstacles


    def avanceVoyageurs(self):
        """Fait avancer tous les voyageurs d'un cran."""
        #print("avanceVoyageurs")
        for voya in self.listVoyageurs:
            voya.avancer()

### Classes ###







