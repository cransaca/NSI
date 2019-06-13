from FouleObject import *
from le_terrain import *
import pygame

color_back=(0,255, 102 )
color_wall=(255,255, 255)

class voyageur_vue:
    """sauvegarde les caractéristiques d'un polygone tkinter"""
    def __init__(self, screen, voyageur_modele):
        self.observe = voyageur_modele
        self.screen = screen
        self.x,self.y = voyageur_modele.getCoord()
        self.affichage_cercle(screen,x,y,(255,0,0))
        voyageur_modele.attacher_observateur(self)

    def mise_a_jour(self):
        self.affichage_cercle(screen,self.x,self.y,color_back)
        self.x,self.y = voyageur_modele.getCoord()
        self.affichage_cercle(screen,self.x,self.y,(255,0,0))
        self.toile.update()

    def affichage_cercle(screen,x,y,color):
            pygame.draw.circle(screen,(0,255,255),(x,y),10)



list_color_people=[(255,0,0), (255,255,0),(255, 102, 0),(102,51, 0),(255, 51, 102),(255,153,51)]

pygame.init()
nb_l, nb_w=100,100
T=Terrain(nb_l, nb_w)
screen = pygame.display.set_mode((900,900))
screen.fill(color_back)

for obst in T.getObjects():
    x,y=obst.getCoord()
    color_wall=(0,0,255)
    #pygame.draw.circle(screen, color_wall, (x,y),10)


pygame.display.update()  #indispensable pour voir s'afficher quelque chose.

done=False
while done==False:
    door=randint(0,4) #choose door
    door=1
    T.creerVoyageur(T.getPorte()[door],T.getPorte()[door+1]) # horizontal va en face
    T.avanceVoyageurs
    for voyageur in T.getObjects():
        x,y=voyageur.getCoord()
        print(x,y)
        color_back=(255,0,0)
        pygame.draw.circle(screen,color_back,(x,y),10)
        #color_voyageur=(255,0,100)
        #pygame.draw.circle(screen,color_voyageur,(x,y),10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done=True
        if pygame.mouse.get_pressed()[0]:
            done=True
    print("pass")

pygame.quit()





