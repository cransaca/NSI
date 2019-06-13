### Importations ###
from math import *
from random import *
from FouleObject import *

### Paramètres ###
### Fonctions ###


### Classes ###

class Terrain():
    """Terrain dans lequel la foule se déplace."""
    def __init__(self, largeur, longueur ,obstacle=[[3,3],[4,7],[8,2]], voyageur=None ):
        # Dimension du terrain
        self.largeur=largeur
        self.longueur=longueur

        # Organisation du terrain
        self.listObstacles=[]
        self.initObstacles(obstacle)

        # Voyageurs
        self.listVoyageurs=[]
        self.initVoyageurs()

        # Affichage texte pour tester
        self.grille=[]
        self.grilleTxt=[]

    def creerObstacle(self, coord):
        """Crée un obstacle."""
        self.listObstacles.append(Obstacle(self,coord))

    def initObstacles(self, obstacle):
        self.creerMurs()
        for obst in obstacle:
            self.creerObstacle(obst)

    def creerMurs(self):
        """Crée les murs du terrain."""
        for i in range(self.largeur):
            self.creerObstacle([i,0])
            self.creerObstacle([i,self.longueur-1])
        for i in range(self.longueur):
            self.creerObstacle([0,i])
            self.creerObstacle([self.largeur-1,i])

    def creerVoyageur(self, coord,destination):
        """Crée un nouveau voyageur."""
        self.listVoyageurs.append(Voyageur(self, coord,destination))

    def initVoyageurs(self):
        self.creerVoyageur([1,1],[8,8])

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

    def majGrille(self):
        self.grille=[]
        self.grilleTxt=[]
        for i in range(self.longueur):
            self.grille.append([])
            self.grilleTxt.append([])
            for j in range(self.largeur):
                self.grille[i].append(None)
                self.grilleTxt[i].append(0)
        for obst in self.listObstacles:
            self.grille[obst.coord[0]][obst.coord[1]]=obst
            self.grilleTxt[obst.coord[0]][obst.coord[1]]=1
        for voya in self.listVoyageurs:
            self.grille[voya.coord[0]][voya.coord[1]]=voya
            self.grilleTxt[voya.coord[0]][voya.coord[1]]=2

    def afficherTexte(self):
        self.majGrille()
        for lig in self.grilleTxt:
            print(lig)

if __name__=="__main__":
    terrain=Terrain(10,10)
    terrain.afficherTexte()
    for i in range(3):
        terrain.avanceVoyageurs()
        terrain.afficherTexte()



