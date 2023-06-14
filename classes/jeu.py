import sys

from classes.interface import *
from classes.gagnant import affiche_gagnant


class Jeu:
  max_jeton = 42

  def __init__(self):
    self.jetons_joues = 0
    self.gagnant = False
    self.grid = Interface()
    self.matrice = Grille()

  def get_joueur(self):
    # pour déterminer le joueur 
    if self.jetons_joues % 2 == 0:
      numero = self.matrice.jeton_noir
    else:
      numero = self.matrice.jeton_blanc
    return numero

  def lancer_jeu(self):
    pygame.init()
    while self.gagnant != "Blanc" and self.gagnant != "Noir" and self.jetons_joues < self.max_jeton:
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          # récuperer la position de la souris sur l'écran
          x, y = pygame.mouse.get_pos()
          # récuperer le joueur courant
          joueur = self.get_joueur()
          # récuperer la colonne joué
          colonne = self.grid.get_colonne(x)
          # placer un jeton
          jetons_joues = self.matrice.jouer_tour(joueur, colonne) #ce n'est pas la meme variable que self.jetons_joués, il s'agit ici d'un attribut de classe
          # vérifier s'il y a un gagnant
          if jetons_joues:
            self.jetons_joues += 1
            self.gagnant = self.matrice.get_gagnant(joueur)
            # afficher de nouveau la grille 
            self.grid.render(self.matrice.matrice) #pour l'affichage des jetons
            self.grid.jeu.display.flip()

        # fermer le jeu
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.QUIT:
          # Quit event
          pygame.quit()
          sys.exit()

    affiche_gagnant(self.gagnant)
