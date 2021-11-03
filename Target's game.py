import pygame
from pygame.locals import *
import sys
import time
import random

BLUE = 0,0,255

pygame.init()

FPS = 150
FPSCLOCK = pygame.time.Clock()
FPSCLOCK.tick(FPS)

fond = pygame.font.Font('freesansbold.ttf', 18)

viseur_image = pygame.image.load('C:\Jeu personnages\OIP (50).png')
bg = pygame.image.load('C:\Jeu personnages\OIP.png')
cible_image = pygame.image.load('C:\Jeu personnages\OIP (58).png')

fenetre = pygame.display.set_mode((700, 490))

pygame.display.set_icon(cible_image)
pygame.display.set_caption('Shoot the targets !')

class Viseur () :
    def __init__ (self) :
        self.x = random.randint(0,600)
        self.y = random.randint(0,400)
        self.image = viseur_image

    def display (self) :
        fenetre.blit(self.image,(self.x, self.y))

class Cible () :
    def __init__ (self) :
        self.x = 0
        self.y = 0
        self.image = cible_image

    def display (self) :
        fenetre.blit(self.image,(self.x, self.y))

viseur1 = Viseur ()
cible1 = Cible ()

start_ticks=pygame.time.get_ticks()
seconds=(pygame.time.get_ticks()-start_ticks)

cible_rect = cible1.image.get_rect(topleft = (cible1.x, cible1.y))

while True :
    seconds=(pygame.time.get_ticks()-start_ticks)/1000

    if seconds == 0.7:
        cibles_affichées += 1
        cible_rect = cible1.image.get_rect(topleft = (cible1.x, cible1.y))
        cible1.x = random.randint(0,600)
        cible1.y = random.randint(0,400)
        start_ticks=pygame.time.get_ticks()
        seconds=(pygame.time.get_ticks()-start_ticks)
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
    
    for event in pygame.event.get():

        if event.type == MOUSEMOTION:
            viseur1.x = event.pos [0] -13
            viseur1.y = event.pos [1] -10
        
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
              
        if event.type == KEYDOWN :            
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            if cible_rect.collidepoint(event.pos [0] -13, event.pos[1] -10) :
                cibles_touchées += 1

    cibles_manquées = cibles_affichées-cibles_touchées
        
    fenetre.blit(bg,(0,0))

    cible1.display()
    viseur1.display()
    
    pygame.display.flip()


