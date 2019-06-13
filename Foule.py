### Importations ###
### Paramètres ###
### Fonctions ###

def conversionPolaireCartesien(r,theta):
    return [x,y]

def convertCartesienPolaire:

### Classes ###

doorWidth=50

class Terrain():
    """Terrain dans lequel la foule se déplace."""
    def __init__(self):
        self.largeur=900
        self.longeur=900

        listAcces=[ [complex(200,self.largeur),complex(200+doorWidth,self.largeur)]]
        listAcces.append([complex(200,0),complex(200+doorWidth,0)])
        listAcces.append([complex(self.longueur,200),complex(self.longueur,200+doorWidth)])
        listAcces.append([complex(0,200),complex(0,200+doorWidth)])

        listObstaclesFixes=[]
        listVoyageurs[]

    def getObstacle

    def creerVoyageur():

    def creerObstacle():

    def avanceVoyageur():

    def bouclePrincipale
        while continue:
            for voyag in self.listVoyageur:
                voyag.positionSuivante


class Obstacle:
    """Les obstacles sont des disques.
        Ils peuvent etre fixes, ou non comme les voyageurs,
        Les murs sont des disques de rayon infini...
    """

    def __init__(self,c):
        self.coordCentre =c
        self.rayon=10
        #forme

    def getPosition(self)
        return(self.coordCenter,self.rayon)
        """Renvoie coordonnées, rayon et forme."""


class Voyageur(Obstacle):
    def __init__():
        #boss

        #coordCentre =[int, int]
        #rayon
        #forme
        self.destination
        self.vitesse
        #vitesseNorme= int # Const  #complexe
        #vitesseAngle
        #vitesseVecteur=[int, int]


        
    def positionsuivante
        listColision

    def colision(self, obstacle):
        return True//False

    def avancer

    def ChangerDirection

    def testFin













