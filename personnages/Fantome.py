import random
from PIL import ImageTk, Image
from Constants import e, l
from Enumerations import Action, Objectif


"""
La classe fantôme représente un agent avec des coordonnées.
"""
class Fantome:
    def __init__(self, background, pacman, cases):
        self.background = background
        self.pacman = pacman
        self.cases = cases
        self.x = 9
        self.y = 4
        self.action = Action.monter
        self.objectif = Objectif.sortir
        fantomeImg = Image.open("images/fantome.jpg").resize((int(l / 2), int(l / 2)), resample=0)
        fantomeImg = ImageTk.PhotoImage(fantomeImg)
        self.image = fantomeImg
        self.sprite = self.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)

    def bouger(self):
        if self.objectif == Objectif.chercher:
            self.action = self.chercher() # cherche pacman
        elif self.objectif == Objectif.sortir:
            self.action = self.sortir()
        elif self.objectif == Objectif.fuir:
            self.action = self.fuir()
        else:
            self.action = self.chercher()
        print(self.x, self.y, self.objectif.name, self.action.name, self.pacman.ticks)
        self.deplacer(self.action) # effectue le déplacement
        self.tuer() # essaye de tuer pacman
        self.mourrir() # s'il doit mourrir meurt

    # objectif: sortir de l'enclos
    def sortir(self):
        if self.y == 2:
            self.objectif = Objectif.chercher
            return self.chercher()
        else:
            return self.action

    # objectif: chercher pacman
    def chercher(self):
        test = False
        if self.pacman.x == self.x: # si self.pacman meme colonne que fantome
            if self.pacman.y > self.y: # si fantome plus haut que self.pacman
                i = self.y
                while i < self.pacman.y and test == False: # est-ce que ya des murs entre ?
                    if self.cases[self.x][i].bas:
                        test = True # => oui
                    i += 1
                if not test:
                    return Action.descendre # => non donc on descend
            else: # sinon fantome plus bas
                i = self.pacman.y
                while i < self.y and test == False:
                    if self.cases[self.x][i].bas:
                        test = True
                    i += 1
                if not test:
                    return Action.monter # => donc on monte
        if self.pacman.y == self.y:
            if self.pacman.x > self.x:
                i = self.x
                while i < self.pacman.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Action.droite # => on va a droite
            else:
                i = self.pacman.x
                while i < self.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    return Action.gauche # => on va a droite
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            self.cases[self.x][self.y].haut == True, # mur == true => true
            self.cases[self.x][self.y].droite == True,
            self.cases[self.x][self.y].gauche == True,
            self.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3) # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3: # si mur == true
            r = random.randint(0, 3) # => relance aléatoire
        return Action(r)

    # mouvement inverse
    def fuir(self):
        test = False
        if self.pacman.x == self.x: # si self.pacman meme colonne que fantome
            if self.pacman.y > self.y: # si fantome plus haut que self.pacman
                i = self.y
                while i < self.pacman.y and test == False: # est-ce que ya des murs entre ?
                    if self.cases[self.x][i].bas:
                        test = True # => oui
                    i += 1
                if self.cases[self.x][self.y].haut:
                    test = True
                if not test:
                    return Action.monter # => non donc on descend
            else: # sinon fantome plus bas
                i = self.pacman.y
                while i < self.y and test == False:
                    if self.cases[self.x][i].bas:
                        test = True
                    i += 1
                if self.cases[self.x][self.y].bas:
                    test = True
                if not test:
                    return Action.descendre # => donc on monte
        if self.pacman.y == self.y:
            if self.pacman.x > self.x:
                i = self.x
                while i < self.pacman.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if self.cases[self.x][self.y].gauche:
                    test = True
                if not test:
                    return Action.gauche # => on va a droite
            else:
                i = self.pacman.x
                while i < self.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if self.cases[self.x][self.y].droite:
                    test = True
                if not test:
                    return Action.droite # => on va a droite
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            self.cases[self.x][self.y].haut == True, # mur == true => true
            self.cases[self.x][self.y].droite == True,
            self.cases[self.x][self.y].gauche == True,
            self.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3) # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3: # si mur == true
            r = random.randint(0, 3) # => relance aléatoire
        return Action(r)

    # objectif: tuer pacman
    def tuer(self):
        if self.objectif == Objectif.chercher:
            if self.pacman.x == self.x and self.pacman.y == self.y:
                self.pacman.mourrir()

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
        self.background.coords(self.sprite, self.x * l + (3 * e), self.y * l + (3 * e))

    def mourrir(self):
        if self.objectif == Objectif.fuir:
            if self.pacman.x == self.x and self.pacman.y == self.y:
                self.x = 9
                self.y = 4
                self.action = Action.monter
                self.objectif = Objectif.sortir
                self.background.coords(self.sprite, self.x * l + (3 * e), self.y * l + (3 * e))