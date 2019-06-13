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

for obst in T.getObstacles():
    x,y=getCoord(obst)
    pygame.draw.rect(screen, color_wall, )


pygame.display.update()  #indispensable pour voir s'afficher quelque chose.

done=False
while done==False:
    door=randint(0,4) #choose door
    door=1
    self.creerVoyageur(self.porte[door],self.porte[door+1]) # horizontal va en face
    self.avanceVoyageurs
    for voyageur in getVoyageurs():
        x,y=getCoord(voyageur)
        pygame.draw.circle(color_back)
        pygame.draw.circle(color_voyageur)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done=True

pygame.quit()





