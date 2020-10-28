import random
from PIL import ImageTk, Image
import Partie
from Constants import l, e
from Enumerations import Action, Objectif
from App import *

fantomeImg = Image.open("images/fantome.jpg").resize((int(l/2), int(l/2)), resample=0)
fantomeImg = ImageTk.PhotoImage(fantomeImg)

"""
La classe fantôme représente un agent avec des coordonnées.
"""
class Fantome:
    def __init__(self):
        self.x = 9
        self.y = 4
        self.action = Action.monter
        self.objectif = Objectif.chercher
        self.image = fantomeImg
        self.sprite = App.background.create_image(self.x*l+(3*e), self.y*l+(3*e), image=self.image)

    def bouger(self):
        self.action = self.chercher() # cherche pacman
        self.deplacer(self.action) # effectue le déplacement
        self.tuer() # essaye de tuer pacman

    # objectif: chercher pacman
    def chercher(self):
        test = False
        if Partie.pacman.x == self.x: # si Partie.pacman meme colonne que fantome
            if Partie.pacman.y > self.y: # si fantome plus haut que Partie.pacman
                i = self.y
                while i < Partie.pacman.y and test == False: # est-ce que ya des murs entre ?
                    if Partie.cases[self.x][i].bas:
                        test = True # => oui
                    i += 1
                if not test:
                    return Action.descendre # => non donc on descend
            else: # sinon fantome plus bas
                i = Partie.pacman.y
                while i < self.y and test == False:
                    if Partie.cases[self.x][i].bas:
                        test = True
                    i += 1
                if not test:
                    return Action.monter # => donc on monte
        if Partie.pacman.y == self.y:
            if Partie.pacman.x > self.x:
                i = self.x
                while i < Partie.pacman.x and test == False:
                    if Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Action.droite # => on va a droite
            else:
                i = Partie.pacman.x
                while i < self.x and test == False:
                    if Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Action.gauche # => on va a droite
        listeActionsPossibles = [
            Partie.cases[self.x][self.y].haut == True, # mur == true => true
            Partie.cases[self.x][self.y].bas == True,
            Partie.cases[self.x][self.y].droite == True,
            Partie.cases[self.x][self.y].gauche == True
        ]
        r = random.randint(0, 3) # aléatoire
        while listeActionsPossibles[r]: # si mur == true
            r = random.randint(0, 3) # => relance aléatoire
        return Action(r)

    # objectif: tuer pacman
    def tuer(self):
        if Partie.pacman.x == self.x and Partie.pacman.y == self.y:
            Partie.pacman.mourrir()


    # action: monter, descendre, droite, gauche
    def deplacer(self, argument):
        if argument == Action.monter:
            self.y -= 1
        elif argument == Action.descendre:
            self.y += 1
        elif argument == Action.droite:
            self.x += 1
        else:
            self.x -= 1
        App.background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))