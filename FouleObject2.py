### Importations ###
from random import *
#from math import *

color_back=(37,253, 233 )  # Backgroud color
color_wall=(255,255, 255)  # Wall color

### Paramètres ###
### Fonctions ###
def signe(x):
    """Renvoie 0, -1 ou +1 selon le signe de x."""
    if x==0:
        return 0
    else:
        return int(x/abs(x))

def egal(aa,bb):
    (a,b)=aa
    (c,d)=bb
    #print ((a,b),(c,d))
    return ((a==c)and(b==d))
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
    def __init__(self,boss, coord, couleur="black"):
        Observable.__init__(self,boss)
        self.boss=boss
        self.coord=coord
        self.couleur=couleur
    def getCoord(self):
        """Renvoie la liste des coordonnées."""
        return self.coord
    def setColor(self,couleur):
        self.couleur=couleur



class Voyageur(Objet):
    """Un objet qui bouge."""
    def __init__(self,boss, coord,destination,couleur="black"):
        Objet.__init__(self, boss, coord)
        self.couleur=couleur
        self.destination=destination
        self.direction=(0,0)
        self.nbPas=0
        
    def getnbPas(self):
        return self.nbPas
        
    def avancer(self):
        """Définit la direction à prendre."""
        x1,y1=self.coord[0], self.coord[1]
        self.direction=(signe(self.destination[0]-x1),signe(self.destination[1]-y1))
        x=self.direction[0]
        y=self.direction[1]
        # list coordinates of possible location after movement.
        listDirections=[(x1+x,y1+y),(x1+signe(x+y),y1+signe(-x+y)),(x1+signe(x-y),y1+signe(x+y)),(x1-y,y1+x),(x1+y,y1-x)]

        # Eliminate occupied squares
        for obj in self.boss.getObjects():
            o=obj.getCoord()
            #print(o)
            if o in listDirections:
                listDirections.remove(o)
        #a=input("hey")
        #définition de la nouvelle direction
        if  listDirections==[]:
            self.coord=(x1,y1)
        else:
            self.nbPas+=1
            if len(listDirections)==1:
                r=0
            else:
                r=0
                alea=15
                if randint(0,alea)==alea:
                    r=randint(0,len(listDirections))
                    if r==len(listDirections):
                        r=1
            self.coord=listDirections[r]

            if egal(self.coord,self.destination):
                self.setColor(color_back)
                self.notifier()
                self.boss.settotalPas(self.boss.totalPas+self.nbPas)
                self.boss.listVoyageurs.remove(self)
                #print("out")

        #print("On avance2",self.coord,self.direction)
        self.notifier()







if __name__=="__main":
    pass

