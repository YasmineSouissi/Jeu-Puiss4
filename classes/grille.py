from classes.gagnant import *


class Grille:
  vide = 0
  jeton_blanc = 1
  jeton_noir = 2
  blanc_gagnant = 4
  noir_gagnant = 8

  def __init__(self):
    self.matrice = [
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
    ]
    self.gagnant_courant = Gagnant(Grille, self.matrice)
  def __str__(self) :
    s=""
    for i in range(6):
      for j in range(7):
        s=s+str(self.matrice[i][j])
      s=s+'\n'
    return  s
    
  def get_gagnant(self,joueur):
    # vérifier tous les cas 
    gagnant = self.gagnant_courant.gagnant_horizental(joueur)
    if gagnant != "":
      return gagnant
    gagnant = self.gagnant_courant.gagnant_vertical(joueur)
    if gagnant != "":
      return gagnant
    gagnant = self.gagnant_courant.gagnant_diagonal(joueur)
    if gagnant != "":
      return gagnant
    else:
      return False

  def jouer_tour(self, joueur, colonne):
    ligne = 5
    jouer = False
    while ligne >= 0 and not jouer:
      if self.matrice[ligne][colonne] == self.vide:
        if joueur ==self.jeton_noir:
          self.matrice[ligne][colonne] =self.jeton_noir
          jouer = True
        elif joueur == self.jeton_blanc:
          self.matrice[ligne][colonne] = self.jeton_blanc
          jouer = True
      if ligne > 0:
        ligne -= 1
      elif ligne == 0 and not jouer: # not jouer : jouer== false
        return False
    print(self) #pour faire l'affichage avec l'str
    return True  # retourne true si vous avez jouer & false si toute la ligne de la colonne est pleine

  def inverser_matrice(self, matrice):
    inverser_matrice = []
    for i in range(5, -1, -1):
      inverser_matrice.append(matrice[i])
    return inverser_matrice
