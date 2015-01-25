__author__ = 'Edwin'
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Hello World!")
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__=="__main__":
    main()