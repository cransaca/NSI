# coding: utf-8
from le_terrain import *
import pygame
import time

color_back=(37,253, 233 )
color_wall=(255,255, 255)
width=800
length=800
nb_cases_l, nb_cases_w=100,100
longueur_rect, largeur_rect= length//nb_cases_l, width//nb_cases_w

def wait():
    event_happened = False
    while not event_happened:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_happened = True

class Voyageur_vue:

    def __init__(self, screen, voyageur_modele,couleur):
        self.observe = voyageur_modele
        self.screen = screen
        self.couleur=couleur
        self.x,self.y = voyageur_modele.getCoord()
        #print("Créer Observateur",self.x,self.y)
        pygame.draw.rect(screen, couleur,[self.x*longueur_rect,self.y*largeur_rect,longueur_rect,largeur_rect],0)
        pygame.display.update()
        voyageur_modele.attacher_observateur(self)# on associe à un voyageur le voyageur vue.

    def mise_a_jour(self,voyageur_modele):
        couleur=voyageur_modele.couleur
        pygame.draw.rect(screen, color_back,[self.x*longueur_rect,self.y*largeur_rect,longueur_rect,largeur_rect],0)
        self.x,self.y = voyageur_modele.getCoord()
        #print("Mise à jour",self.x,self.y)
        pygame.draw.rect(screen, couleur,[self.x*longueur_rect,self.y*largeur_rect,longueur_rect,largeur_rect],0)
        pygame.display.update()

screen = pygame.display.set_mode((length,width))
screen.fill(color_back)
list_color_people=[(255,0,0), (255,255,0),(255, 102, 0),(102,51, 0),(255, 51, 102),(255,153,51)]


T=Terrain(nb_cases_w, nb_cases_l)

for obst in T.getObjects():
            x,y=obst.getCoord()
            pygame.draw.rect(screen, color_wall,[x*longueur_rect,y*largeur_rect,longueur_rect,largeur_rect],0)

pygame.display.update()  #indispensable pour voir s'afficher quelque chose.



done=False
n=0
door=1
T.creerVoyageur(T.getPorte()[0],T.getPorte()[1]) # horizontal va en face

while done==False:
            #print("begin")
            doorin=randint(0,3) #choose door
            doorout=randint(0,3)
            while doorout==doorin:
                doorout=randint(0,3) #choose door
            color=randint(0,5)
            #door=1
            T.creerVoyageur(T.getPorte()[doorin],T.getPorte()[doorout],list_color_people[color]) # horizontal va en face
            listObservateurs=[]
            for obs in T.getVoyageurs():
                listObservateurs.append(Voyageur_vue(screen,obs,obs.couleur))
            print ("loop",len(listObservateurs))
            #print("Avance Voyageurs")
            T.avanceVoyageurs()
            n=0
            for voyageur in T.getVoyageurs():
                x,y=voyageur.getCoord()
                #print("Liste Voyageurs",n,x,y)
                n=n+1

                #color_voyageur=(255,0,100)
                #pygame.draw.circle(screen,color_voyageur,(x,y),10)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done=True
                if pygame.mouse.get_pressed()[0]:
                    done=True
            n+=1
            if (n>100):
                done=True
            #time.sleep(0.01)
pygame.quit()




