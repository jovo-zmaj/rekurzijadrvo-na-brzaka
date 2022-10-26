import pygame, sys
from pygame.locals import QUIT

pygame.init()
EKRAN = pygame.display.set_mode((400, 300))
pygame.display.set_caption('cao')

def rek():
	pass


def main():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()

main()