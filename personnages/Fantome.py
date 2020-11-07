import random
from PIL import ImageTk, Image
import Partie
import Constants
import Enumerations
import App


"""
La classe fantôme représente un agent avec des coordonnées.
"""
class Fantome:
    def __init__(self):
        self.x = 9
        self.y = 4
        self.action = Enumerations.Action.monter
        self.objectif = Enumerations.Objectif.sortir
        fantomeImg = Image.open("images/fantome.jpg").resize((int(Constants.l / 2), int(Constants.l / 2)), resample=0)
        fantomeImg = ImageTk.PhotoImage(fantomeImg)
        self.image = fantomeImg
        self.sprite = App.App.background.create_image(self.x*Constants.l+(3*Constants.e), self.y*Constants.l+(3*Constants.e), image=self.image)
        self.alive = True

    def bouger(self):
        if self.objectif == Enumerations.Objectif.chercher:
            self.action = self.chercher() # cherche pacman
        elif self.objectif == Enumerations.Objectif.sortir:
            self.action = self.sortir()
        elif self.objectif == Enumerations.Objectif.fuir:
            self.action = self.fuir()
        else:
            self.action = self.chercher()
        print(self.x, self.y, self.objectif.name, self.action.name, Partie.Partie.pacman.ticks)
        self.deplacer(self.action) # effectue le déplacement
        self.tuer() # essaye de tuer pacman

    # objectif: sortir de l'enclos
    def sortir(self):
        if self.y == 2:
            self.objectif = Enumerations.Objectif.chercher
            return self.chercher()
        else:
            return self.action

    # objectif: chercher pacman
    def chercher(self):
        test = False
        if Partie.Partie.pacman.x == self.x: # si Partie.Partie.pacman meme colonne que fantome
            if Partie.Partie.pacman.y > self.y: # si fantome plus haut que Partie.Partie.pacman
                i = self.y
                while i < Partie.Partie.pacman.y and test == False: # est-ce que ya des murs entre ?
                    if Partie.Partie.cases[self.x][i].bas:
                        test = True # => oui
                    i += 1
                if not test:
                    return Enumerations.Action.descendre # => non donc on descend
            else: # sinon fantome plus bas
                i = Partie.Partie.pacman.y
                while i < self.y and test == False:
                    if Partie.Partie.cases[self.x][i].bas:
                        test = True
                    i += 1
                if not test:
                    return Enumerations.Action.monter # => donc on monte
        if Partie.Partie.pacman.y == self.y:
            if Partie.Partie.pacman.x > self.x:
                i = self.x
                while i < Partie.Partie.pacman.x and test == False:
                    if Partie.Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Enumerations.Action.droite # => on va a droite
            else:
                i = Partie.Partie.pacman.x
                while i < self.x and test == False:
                    if Partie.Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Enumerations.Action.gauche # => on va a droite
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            Partie.Partie.cases[self.x][self.y].haut == True, # mur == true => true
            Partie.Partie.cases[self.x][self.y].droite == True,
            Partie.Partie.cases[self.x][self.y].gauche == True,
            Partie.Partie.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3) # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3: # si mur == true
            r = random.randint(0, 3) # => relance aléatoire
        return Enumerations.Action(r)

    # mouvement inverse
    def fuir(self):
        test = False
        if Partie.Partie.pacman.x == self.x: # si Partie.Partie.pacman meme colonne que fantome
            if Partie.Partie.pacman.y > self.y: # si fantome plus haut que Partie.Partie.pacman
                i = self.y
                while i < Partie.Partie.pacman.y and test == False: # est-ce que ya des murs entre ?
                    if Partie.Partie.cases[self.x][i].bas:
                        test = True # => oui
                    i += 1
                if Partie.Partie.cases[self.x][self.y].haut:
                    test = True
                if not test:
                    return Enumerations.Action.monter # => non donc on descend
            else: # sinon fantome plus bas
                i = Partie.Partie.pacman.y
                while i < self.y and test == False:
                    if Partie.Partie.cases[self.x][i].bas:
                        test = True
                    i += 1
                if Partie.Partie.cases[self.x][self.y].bas:
                    test = True
                if not test:
                    return Enumerations.Action.descendre # => donc on monte
        if Partie.Partie.pacman.y == self.y:
            if Partie.Partie.pacman.x > self.x:
                i = self.x
                while i < Partie.Partie.pacman.x and test == False:
                    if Partie.Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if Partie.Partie.cases[self.x][self.y].gauche:
                    test = True
                if not test:
                    return Enumerations.Action.gauche # => on va a droite
            else:
                i = Partie.Partie.pacman.x
                while i < self.x and test == False:
                    if Partie.Partie.cases[i][self.y].droite:
                        test = True
                    i += 1
                if Partie.Partie.cases[self.x][self.y].droite:
                    test = True
                if not test:
                    return Enumerations.Action.droite # => on va a droite
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            Partie.Partie.cases[self.x][self.y].haut == True, # mur == true => true
            Partie.Partie.cases[self.x][self.y].droite == True,
            Partie.Partie.cases[self.x][self.y].gauche == True,
            Partie.Partie.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3) # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3: # si mur == true
            r = random.randint(0, 3) # => relance aléatoire
        return Enumerations.Action(r)

    # objectif: tuer pacman
    def tuer(self):
        if Partie.Partie.pacman.x == self.x and Partie.Partie.pacman.y == self.y:
            Partie.Partie.pacman.mourrir()

    # action: monter, descendre, droite, gauche
    def deplacer(self, argument):
        if argument == Enumerations.Action.monter:
            self.y -= 1
        elif argument == Enumerations.Action.descendre:
            self.y += 1
        elif argument == Enumerations.Action.droite:
            self.x += 1
        else:
            self.x -= 1
        App.App.background.coords(self.sprite, self.x*Constants.l+(3*Constants.e), self.y*Constants.l+(3*Constants.e))
        if Partie.Partie.pacman.x == self.x and Partie.Partie.pacman.y == self.y and Enumerations.Objectif.fuir:
            App.App.background.delete(self.sprite)
            self.alive = False