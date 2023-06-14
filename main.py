# import modules
import pygame
from classes.jeu import Jeu

pygame.init()

# Screen
window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Puissance 4")

#pour changer l'icone pygame
programIcon = pygame.image.load('images/our.ico')
pygame.display.set_icon(programIcon)


def jouer_puiss():
  jeu = Jeu()
  jeu.lancer_jeu()


jouer_puiss()
