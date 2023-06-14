import tkinter
from tkinter import *

# Classe Gagnant
class Gagnant:

  def __init__(self, matrice, grille_tab):
    self.matrice = matrice
    self.grille_tab = grille_tab

  def gagnant_horizental(self,joueur):
    # Pas gagnant au début
    gagnant = ""
    # 6 lignes 
    ligne = 5
    # pour arreter la boucle
    fin_jeu = False
    # vérifier tous lignes pour trouver le gagnant 
    while ligne >= 0 and not fin_jeu:
      for colonne in range(4):
        if(self.grille_tab[ligne][colonne]==joueur):
          if self.verif_horizental(ligne, colonne) == self.matrice.noir_gagnant:
            gagnant = "Noir"
            fin_jeu = True
          if self.verif_horizental(ligne, colonne) == self.matrice.blanc_gagnant:
            gagnant = "Blanc"
            fin_jeu = True
      ligne -= 1
    # retourne la variable gagnant
    return gagnant

  def gagnant_vertical(self,joueur):
    
    gagnant = ""
    # 7 colonnes
    colonne = 6
    fin_jeu = False
    # vérifier tous colonnes pour trouver le gagnant 
    while colonne >= 0 and not fin_jeu:
      for ligne in range(3):
        if(self.grille_tab[ligne][colonne]==joueur):
          if self.verif_vertical(ligne, colonne) == self.matrice.noir_gagnant:
            fin_jeu = True
            gagnant = "Noir"
          if self.verif_vertical(ligne, colonne) == self.matrice.blanc_gagnant:
            fin_jeu = True
            gagnant = "Blanc"
      colonne -= 1
    return gagnant

  def gagnant_diagonal(self,joueur):
    # parcourt de la matrice du haut gauche vers le bas à droite
    gagnant = ""
    for ligne in range(3):
      for colonne in range(4):
        if(self.grille_tab[ligne][colonne]==joueur):
          if self.verif_diagonal(ligne, colonne, True) == self.matrice.noir_gagnant:
            gagnant = "Noir"
          if self.verif_diagonal(ligne, colonne, True) == self.matrice.blanc_gagnant:
            gagnant = "Blanc"
    # parcourt de la matrice du haut droit vers le bas à gauche
    for ligne in range(3):
      for colonne in range(3, 7):
        if(self.grille_tab[ligne][colonne]==joueur):
          if self.verif_diagonal(ligne, colonne, False) == self.matrice.noir_gagnant:
            gagnant = "Noir"
          if self.verif_diagonal(ligne, colonne, False) == self.matrice.blanc_gagnant:
            gagnant = "Blanc"
    return gagnant

  def verif_horizental(self, ligne, colonne):
    if (self.grille_tab[ligne][colonne] == self.grille_tab[ligne][colonne + 1] ==self.grille_tab[ligne][colonne + 2] ==self.grille_tab[ligne][colonne + 3]) and (self.grille_tab[ligne][colonne] !=0):
      return self.grille_tab[ligne][colonne] + self.grille_tab[ligne][colonne + 1] + self.grille_tab[ligne][colonne + 2] + self.grille_tab[ligne][colonne + 3]
    else:
      return 0




  """def verif_vertical(self, ligne, colonne):
    #s=self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne] + self.grille_tab[ligne + 2][colonne] + self.grille_tab[ligne + 3][colonne]
    #print("vertical:::" )
    #print(s)
    if (self.grille_tab[ligne][colonne] == self.grille_tab[ligne + 1][colonne] == self.grille_tab[ligne + 2][colonne] + self.grille_tab[ligne + 3][colonne]) and (self.grille_tab[ligne][colonne]!=0):
      return self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne] + self.grille_tab[ligne + 2][colonne] + self.grille_tab[ligne + 3][colonne]
    else:
      return 0"""

      
  def verif_vertical(self, ligne, colonne):
    #s=self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne] + self.grille_tab[ligne + 2][colonne] + self.grille_tab[ligne + 3][colonne]
    #print("vertical:::" )
    #print(s)
    return self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne] + self.grille_tab[ligne + 2][colonne] + self.grille_tab[ligne + 3][colonne]


  def verif_diagonal(self, ligne, colonne, gauche):
    if gauche:
      #s=self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne + 1] + self.grille_tab[ligne + 2][colonne + 2] + self.grille_tab[ligne + 3][colonne + 3]
      #print("diagonal1:::" )
      #print(s)
      if (self.grille_tab[ligne][colonne] == self.grille_tab[ligne + 1][colonne + 1] ==self.grille_tab[ligne + 2][colonne + 2] == self.grille_tab[ligne + 3][colonne + 3]):
        return self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne + 1] + self.grille_tab[ligne + 2][colonne + 2] + self.grille_tab[ligne + 3][colonne + 3]
      else :
        return 0
    else:
      #s=self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne - 1] + self.grille_tab[ligne + 2][colonne - 2] + self.grille_tab[ligne + 3][colonne - 3]
      #print("diagonal2:::" )
      #print(s)
      if(self.grille_tab[ligne][colonne] == self.grille_tab[ligne + 1][colonne - 1] ==self.grille_tab[ligne + 2][colonne - 2] == self.grille_tab[ligne + 3][colonne - 3]):
        return self.grille_tab[ligne][colonne] + self.grille_tab[ligne + 1][colonne - 1] + self.grille_tab[ligne + 2][colonne - 2] + self.grille_tab[ligne + 3][colonne - 3]
      else:
        return 0


def affiche_gagnant(gagnant):
  # pour afficher le gagnant à la fin du jeu
  fenetre2  = tkinter.Tk() 
  fenetre2.title("Jouer à Puissance4")
  fenetre2.geometry("550x400")
  fenetre2.minsize(480,360)
  fenetre2.iconbitmap("images/our.ico")
  fenetre2.config(background='#794d14')
  #frame
  frame=tkinter.Frame(fenetre2 ,bg='#794d14') #3d270e
  #titre
  label_titre= Label(frame,text="le joueur ayant le jeton "+gagnant+" a gagné",font=("Georgia",20),bg='#794d14',fg='#ffffff')
  label_titre.pack(pady=30)
    
  #ajouter le frame
  frame.pack(expand=YES)
  #afficher
  fenetre2 .mainloop()

  if gagnant == "Noir":
    print("Noir a gagné")
  elif gagnant == "Blanc":
   print("Blanc a gagné")
  else:
   print("Match nul")
