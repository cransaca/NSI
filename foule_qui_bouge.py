# coding: utf-8
color_back=(37,253, 233 )  # Backgroud color
color_wall=(255,255, 255)  # Wall color
width=800
length=800
nb_cases_l, nb_cases_w=80,80

# Defines size of individual cell
longueur_rect, largeur_rect= length//nb_cases_l, width//nb_cases_w


# coding: utf-8
### Importations ###
from math import *
from random import *
import pygame

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

def dist(P1,P2):
    """Renvoie la distance entre 2 points P1 et P2."""
    (a,b)=P1
    (c,d)=P2
    return sqrt((a-c)**2+(b-d)**2)
   


#A function to stop the program
def wait():
    event_happened = False
    while not event_happened:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_happened = True
    
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



### Classes ###
class Terrain():
    """Terrain dans lequel la foule se dÃ©place."""
    def __init__(self, largeur, longueur,choice):#,obstacle=None, voyageur=None ):
        # Dimension du terrain
        self.largeur=largeur
        self.longueur=longueur

        # Organisation du terrain
        self.listObstacles=[]
        self.porte=[]
        self.AjouterPorte((0,self.longueur//2),10)
        self.AjouterPorte((self.largeur-1,self.longueur//2),10)
        self.AjouterPorte((self.largeur//2,0),10)
        self.AjouterPorte((self.largeur//2,self.longueur-1),10)


        self.creerMurs()
        self.initObstacles(choice)
        # Voyageurs
        self.listVoyageurs=[]
        self.totalPas=0
    
    def settotalPas(self,totalPas):
        self.totalPas=totalPas
    
    def gettotalPas(self):
        return(self.totalPas)

    def AjouterPorte(self,coord,radius):
        for i in range(self.largeur):
            if dist((i,self.longueur-1),coord)<radius:

                self.porte.append((i,self.longueur-1))
            if dist((i,0),coord)<radius:

                self.porte.append((i,0))
        for i in range(self.longueur):
            if dist((self.largeur-1,i),coord)<radius:

                self.porte.append((self.largeur-1,i))
            #print("point=",(0,i),"center=",coord,"dist=",dist((0,i),coord),radius)
            if dist((0,i),coord)<radius:

                self.porte.append((0,i))
        #print("nbporte",len(self.porte))
        #print(self.porte)
        #print()

    def nbPorte(self):
        return len(self.porte)

    def getPorte(self):
        return self.porte

    def initObstacles(self,choice):
        #self.creerObstaclesDisque((20,20),5)
        if choice>0:
            #self.creerObstaclesDisque((self.longueur//2,self.largeur//2),5)
            self.creerObstaclesDisque((self.longueur//2-7,self.largeur//2-7),5)
            self.creerObstaclesDisque((self.longueur//2+7,self.largeur//2+7),5)
            self.creerObstaclesDisque((self.longueur//2-7,self.largeur//2+7),5)
            self.creerObstaclesDisque((self.longueur//2+7,self.largeur//2-7),5)        
    
        if choice>1:            
            self.creerObstaclesDisque((self.longueur//2,self.largeur//2-14),5)
            self.creerObstaclesDisque((self.longueur//2+14,self.largeur//2),5)
            self.creerObstaclesDisque((self.longueur//2,self.largeur//2+14),5)
            self.creerObstaclesDisque((self.longueur//2-14,self.largeur//2),5)
            
        if choice>2:
            self.creerObstaclesDisque((self.longueur//4,self.largeur//4),5)
            self.creerObstaclesDisque((3*self.longueur//4,self.largeur//4),5)        
            self.creerObstaclesDisque((self.longueur//4,3*self.largeur//4),5)
            self.creerObstaclesDisque((3*self.longueur//4,3*self.largeur//4),5)
            

    def creerObstaclesDisque(self,coord,radius):
        #print("disque")
        (x,y)=coord
        for i in range(-radius,radius):
            for j in range(-radius,radius):
                if dist((i,j),(0,0))<radius/2.0:
                    #print("obstacle")
                    self.creerObstacle((x+i,y+j))

    def creerObstacle(self, coord):
        """CrÃ©e un obstacle."""
        #print(coord)
        self.listObstacles.append(Objet(self,coord))

    def creerVoyageur(self, coord,destination,couleur=(255,0,0)):
        """Crée un nouveau voyageur."""
        v=Voyageur(self, coord,destination,couleur)
        self.listVoyageurs.append(v)
    def lastVoyageur(self):
        return self.listVoyageurs[len(self.listVoyageurs)-1]
    def nbVoyageurs(self):
        return len(self.listVoyageurs)

    def creerMurs(self):
        #print(self.porte)
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




class Voyageur_vue:
    def __init__(self, screen, voyageur_modele):
        self.observe = voyageur_modele
        self.screen = screen
        self.x,self.y = voyageur_modele.getCoord()
        self.mise_a_jour(voyageur_modele)
        voyageur_modele.attacher_observateur(self)# on associe à un voyageur le voyageur vue.

    def mise_a_jour(self,voyageur_modele):
        couleur=voyageur_modele.couleur
        pygame.draw.rect(screen, color_back,[self.x*longueur_rect,self.y*largeur_rect,longueur_rect,largeur_rect],0)
        self.x,self.y = voyageur_modele.getCoord()
        #print("Mise à jour",self.x,self.y)
        #pygame.draw.rect(screen, couleur,[self.x*longueur_rect,self.y*largeur_rect,longueur_rect,largeur_rect],0)
        rayon=int(sqrt(2*largeur_rect**2)/2)-3
        pygame.draw.circle(screen, couleur,[self.x*longueur_rect+longueur_rect//2,self.y*largeur_rect+largeur_rect//2],rayon,0)
        pygame.display.update()



description=["Modele sans obstacle","Modele avec 5 obstacles", "Modele avec 9 obstacles", "Modele avec 13 obstacles"]

for choice in range(4):

    print(description[choice])

    screen = pygame.display.set_mode((length,width))
    screen.fill(color_back)
    list_color_people=[(255,0,0), (255,255,0),(255, 102, 0),(102,51, 0),(255, 51, 102),(255,153,51)]

    T=Terrain(nb_cases_w, nb_cases_l,choice)

    for obst in T.getObjects():
        x,y=obst.getCoord()
        pygame.draw.rect(screen, color_wall,[x*longueur_rect,y*largeur_rect,longueur_rect,largeur_rect],0)

    pygame.display.update()  #indispensable pour voir s'afficher quelque chose.

    done=False
    n=0
    #door=1
    #wait()
    #T.creerVoyageur(T.getPorte()[0],T.getPorte()[1]) # horizontal va en face

    n=0
    nmax=200
    listObservateurs=[]

    total_distance=0
    
    while done==False:
            nbDoor=T.nbPorte()
            nbCreation=20
            for k in range(nbCreation):
                #print("begin")
                doorin=randint(0,nbDoor-1) #choose door
                doorout=randint(0,nbDoor-1)

                # make sure exit door is not entrance
                while dist(T.getPorte()[doorin],T.getPorte()[doorout])<nb_cases_l-10:
                    doorout=randint(0,nbDoor-1) #choose door
                #color=randint(0,5) # choose random color
                #door=1
                #print(doorin, doorout,nbDoor)
                # Create a voyageur
                if (n<nmax):
                    T.creerVoyageur(T.getPorte()[doorin],T.getPorte()[doorout],list_color_people[doorin%6]) # horizontal va en face
                    listObservateurs.append(Voyageur_vue(screen,T.lastVoyageur()))
                    total_distance+=dist(T.getPorte()[doorin],T.getPorte()[doorout])
                    n=n+1

            #print ("loop",len(listObservateurs))
            #print("Avance Voyageurs")
            T.avanceVoyageurs()
            #wait()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done=True
                #if pygame.mouse.get_pressed()[0]:
                    #done=True
                if event.type == pygame.QUIT:
                    done=True
            #if (n>1000):
            #    done=True
            #time.sleep(0.1)


            if T.nbVoyageurs()==0:
                done=True
    print (" Nombre total de voyageurs",n)
    print (" Nombre total de pas",T.gettotalPas())
    
    print(" Nombre moyen de pas par voyageur", T.gettotalPas()/n)

    pygame.quit()
