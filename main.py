import pygame, sys, math
from pygame.locals import QUIT

pygame.init()
xE=1000
yE=1000
EKRAN = pygame.display.set_mode((xE, yE))
pygame.display.set_caption('cao')

glu=1.5

def rek(u,d,x,y):
	if d<2: return
	su=d*math.sin(u)
	cu=d*math.cos(u)
	pygame.draw.line(EKRAN,(255,255,255),(x,y),(x+su,y-cu),2)	
	#crtaj
	rek(u+glu,d/1.5,x+su,y-cu)
	rek(u-glu,d/1.5,x+su,y-cu)
	return


def main():
        rek(0,yE/4,xE/2,yE)
        pygame.display.update()
        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
			
main()
