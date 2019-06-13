### Importations ###
from math import *
### ParamÃ¨tres ###
### Fonctions ###




### Classes ###

class Terrain():
    """Terrain dans lequel la foule se dÃ©place."""
    def __init__(self, largeur, longueur,obstacle=None, voyageur=None ):
        # Dimension du terrain
        self.largeur=largeur
        self.longueur=longueur

        # Organisation du terrain
        self.listAcces=[]
        self.listObstacles=[]
        self.initObstacleFixes(self)  # initialiser liste des obstacles

        # Voyageurs
        self.listVoyageurs=[]



        # Go !
        self.bouclePrincipale()



    def initObstacleFixes(self):
        """Initialise le terrain avant l'arrivÃ©e des voyageurs."""
        self.creerObstacles([3,3])
        self.creerObstacles([4,4])
        self.creerObstacles([8,2])

    def creerObstacle(self, coord):
        """CrÃ©e un obstacle."""
        self.listObstacles.append(Obstacle(self,coord))

    def creerVoyageur(self, coord,destination):
        """CrÃ©e un nouveau voyageur."""
        self.listVoyageurs.append(Voyageur(self,coord, destination))


    def avanceVoyageur(self):
        """Fait avancer tous les voyageurs d'un cran."""
        for voya in self.listVoyageurs:
            voya.avance()

    def bouclePrincipale():
        while True:
            self.creerVoyageur([7,7])


class Obstacle:
    """Les obstacles sont des disques, qui peuvent etre fixes, ou non comme les voyageurs,
        Les murs sont des disques de rayon infini...
        boss=Terrain , centre=complex , rayon=float
        *forme="disque","carrÃ©" ou "murN","murS","murE","murW" #sert uniquement pour l'affichage
        *couleur
    """
    def __init__(self,boss, centre,rayon,forme="voyageur", arrivee=None, )):
        self.boss=boss # Terrain dans lequel se trouve l'obstacle

        self.coordCentre=centre
        self.rayon=rayon
        self.forme=forme

        self.couleur=couleur


        self.arrivee=arrivee

        self.vitesseNorme= int # Const
        self.vitesseAngle
        self.vitesseVecteur=[int, int]

        positionSuivante
        listColision


    def getEtat(self):
        """Renvoie un dictionnaire avec le centre, le rayon et la forme de l'obstacle."""
        return {"centre":self.centre, "rayon":self.rayon, "forme":self.forme}



    def colision(self, obstacle):
        return True//False

    def avancer

    def ChangerDirection

    def testFin





terrain=Terrain(10 10,obstacle=None, voyageur=None )







