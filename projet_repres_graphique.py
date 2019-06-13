# coding: utf-8
from le_terrain import *
import pygame
import time

color_back=(0,0, 0 )
color_wall=(255,255, 255)

def wait():
    event_happened = False
    while not event_happened:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_happened = True

class Voyageur_vue:
    """sauvegarde les caractéristiques d'un polygone tkinter"""
    def __init__(self, screen, voyageur_modele):
        self.observe = voyageur_modele
        self.screen = screen
        self.x,self.y = voyageur_modele.getCoord()
        #print("Créer Observateur",self.x,self.y)
        pygame.draw.rect(screen, (100,0,0),[self.x*6,self.y*6,6,6],0)
        pygame.display.update()
        voyageur_modele.attacher_observateur(self)# on associe à un voyageur le voyageur vue. 

    def mise_a_jour(self,voyageur_modele):
        pygame.draw.rect(screen, (0,0,0),[self.x*6,self.y*6,6,6],0)
        self.x,self.y = voyageur_modele.getCoord()
        #print("Mise à jour",self.x,self.y)
        pygame.draw.rect(screen, (100,100,100),[self.x*6,self.y*6,6,6],0)
        pygame.display.update()

screen = pygame.display.set_mode((650,650))
screen.fill(color_back)
#list_color_people=[(255,0,0), (255,255,0),(255, 102, 0),(102,51, 0),(255, 51, 102),(255,153,51)]

nb_l, nb_w=100,100
T=Terrain(nb_l, nb_w)

for obst in T.getObjects():
            x,y=obst.getCoord()
            color_wall=(0,100,100)
            pygame.draw.rect(screen, color_wall,[x*6,y*6,6,6],0)

pygame.display.update()  #indispensable pour voir s'afficher quelque chose.



done=False
n=0
door=1
T.creerVoyageur(T.getPorte()[0],T.getPorte()[1]) # horizontal va en face
            
while done==False:
            #print("begin")
            doorin=randint(0,3) #choose door
            doorout=randint(0,3) #choose door
            #door=1
            T.creerVoyageur(T.getPorte()[doorin],T.getPorte()[doorout]) # horizontal va en face
            listObservateurs=[]
            for obs in T.getVoyageurs():
                listObservateurs.append(Voyageur_vue(screen,obs))
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




