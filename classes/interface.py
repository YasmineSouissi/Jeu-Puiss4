import pygame
import tkinter
from tkinter import *
from classes.grille import Grille


class Interface:
  def nouvelle_partie(self):
    self.fenetre.destroy()
    self.joueur = 1
    self.plateau = Grille()#creation d'objet grille
    # on initialise pygame une seule fois
    self.jeu = pygame
    self.colonne = 0
    pygame.init()
    # Taille du plateau
    self.image_grille = self.jeu.image.load('images/grid.png')
    width = self.image_grille.get_size()
    self.board_width = (width[0], width[1])
    # Set notre écran de jeu
    self.screen = self.jeu.display.set_mode(self.board_width)
    self.screen.blit(self.image_grille, (0, 0))
    self.jeu.display.flip()

    # image du jeton blanc
    self.image_jeton_blanc = self.jeu.image.load('images/white.png')
    # image du jeton noir
    self.image_jeton_noir = self.jeu.image.load('images/black.png')
    # Font
    self.font = self.jeu.font.Font(None, 25)


  def fenetre_acceuil(self):
    #creation de la fenetre 
    self.fenetre  = tkinter.Tk() 
    self.fenetre.title("Jouer à Puissance4")
    self.fenetre.geometry("500x400")
    self.fenetre.minsize(480,360)
    self.fenetre.iconbitmap("images/our.ico")
    self.fenetre.config(background='#ffffff')
    #image de font
    """c=Canvas(self.fenetre,height=480,width=360)
    image_font=PhotoImage(file="images/fontt.png")
    font_label=Label(self.fenetre,image=image_font)
    font_label.place(x=0,y=0 ,relwidth=1,relheight=1)
    c.pack()"""

    #frame
    frame=tkinter.Frame(self.fenetre ,bg='#ffffff')
    #titre
    label_titre= Label(frame,text="PUISSANCE4",font=("Georgia",30),bg='#ffffff',fg='#3d270e')
    label_titre.pack(pady=30)
    #bouton de demarrage du jeu
    bouton= Button(frame,text="Démarrer une nouvelle partie",font=("Comic Sans MS",15),pady=20,padx=25,fg='#3d270e',bg='#c5ad97',command=self.nouvelle_partie)
    bouton.pack(pady=20)
    #ajouter le frame
    frame.pack(expand=YES)
    #afficher
    self.fenetre .mainloop()
  
  def __init__(self) :
    self.fenetre_acceuil()

    
  def get_colonne(self, numero):
    colonne = numero - 16
    colonne = int(colonne / 100)
    if colonne in range(0, 7):
      if self.plateau.matrice[5][int(colonne)] == 0:
        self.colonne = colonne
    return colonne

  def render(self, matrice):#necessaire pour l'affichage
    # rafraichir l'ecran
    self.screen.fill((0, 0, 0))
    self.screen.blit(self.image_grille, (0, 0))
    # inverser_matrice() pour inverser la matrice
    inverse = self.plateau.inverser_matrice(matrice)
   
    for i in range(len(inverse)):
      for j in range(len(inverse[i])):
        # affichage jeton Noir 
        if inverse[i][j] == self.plateau.jeton_noir:
          self.screen.blit(self.image_jeton_noir, (16 + 97 * j, 13 - 97 * i + 486))
        self.jeu.display.flip()
        # affichage jeton Blanc 
        if inverse[i][j] == self.plateau.jeton_blanc:
          self.screen.blit(self.image_jeton_blanc, (16 + 97 * j, 13 - 97 * i + 486))
        self.jeu.display.flip()
