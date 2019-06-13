from le_terrain import *
import pygame

color_back=(0,255, 102 )
color_wall=(255,255, 255)

list_color_people=[(255,0,0), (255,255,0),(255, 102, 0),(102,51, 0),(255, 51, 102),(255,153,51)]
pygame.init()
nb_l, nb_w=100,100
T=Terrain(nb_l, nb_w)
screen = pygame.display.set_mode((900,900))
screen.fill(color_back)

for obst in T.getObjects():
    x,y=obst.getCoord()
    pygame.draw.circle(screen, color_wall, (x,y),10)


pygame.display.update()  #indispensable pour voir s'afficher quelque chose.

done=False
while done==False:
    door=randint(0,4) #choose door
    door=1
    T.creerVoyageur(T.getPorte()[door],T.getPorte()[door+1]) # horizontal va en face
    T.avanceVoyageurs
    for voyageur in T.getObjects():
        x,y=voyageur.getCoord()
        pygame.draw.circle(screen,color_back,(x,y),10)
        color_voyageur=(255,0,255)
        pygame.draw.circle(screen,color_voyageur,(x,y),10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done=True

pygame.quit()





