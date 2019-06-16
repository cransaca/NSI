# coding: utf-8
color_back=(37,253, 233 )  # Backgroud color
color_wall=(255,255, 255)  # Wall color
width=800
length=800
nb_cases_l, nb_cases_w=80,80

from le_terrain import *
import pygame
import time

# Defines size of individual cell
longueur_rect, largeur_rect= length//nb_cases_l, width//nb_cases_w

#A function to stop the program
def wait():
    event_happened = False
    while not event_happened:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_happened = True

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



description=["Modele sans obstacle","Modele avec 4 obstacles", "Modele avec 8 obstacles"]

for choice in range(3):

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
    nmax=500
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
                while dist(T.getPorte()[doorin],T.getPorte()[doorout])<20:
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
