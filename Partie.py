from typing import List

from PIL import ImageTk, Image

from Constants import l, e
from Enumerations import Status, Objectif
from labyrinthe.Case import Case
from labyrinthe.Gomme import Gomme
from personnages.Fantome import Fantome
from personnages.PacMan import PacMan

"""
Création d'une partie. Une partie est une instance recréable si PacMan meurt ou gagne.
Elle instancie Pacman, les Fantomes, les cases avec leurs attributs (gomme) ainsi que la "loop" de la
partie pour que cela fonctionne.
"""
class Partie:

    def __init__(self, window, background, statusPartie):
        self.window = window
        self.background = background
        self.statusPartie = statusPartie
        self.cases = []
        self.pacman = None
        self.fantomes = []
        self.ticks = 1
        self.victoryImg = Image.open("images/Victory.jpg")
        self.victoryImg = ImageTk.PhotoImage(self.victoryImg)
        self.defeatImg = Image.open("images/GameOver.jpg")
        self.defeatImg = ImageTk.PhotoImage(self.defeatImg)
        self.endscreen = None
        # Labyrinthe
        self.cases = []
        for x in range(0, 18):
            self.cases.append([])
        # ligne 1
        self.cases[0].append(Case(0, 0, True, False, False, True, Gomme.vide, background))
        for x in range(1, 3):
            self.cases[x].append(Case(x, 0, True, True, False, False, Gomme.gomme, background))
        self.cases[3].append(Case(3, 0, True, False, True, False, Gomme.gomme, background))
        self.cases[4].append(Case(4, 0, False, False, True, True, Gomme.vide, background))
        self.cases[5].append(Case(5, 0, True, False, False, True, Gomme.gomme, background))
        for x in range(6, 12):
            self.cases[x].append(Case(x, 0, True, True, False, False, Gomme.gomme, background))
        self.cases[12].append(Case(12, 0, True, False, True, False, Gomme.gomme, background))
        self.cases[13].append(Case(13, 0, False, False, True, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 0, True, False, False, True, Gomme.gomme, background))
        for x in range(15, 17):
            self.cases[x].append(Case(x, 0, True, True, False, False, Gomme.gomme, background))
        self.cases[17].append(Case(17, 0, True, False, True, False, Gomme.gomme, background))
        # ligne 2
        self.cases[0].append(Case(0, 1, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 1, True, False, False, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 1, True, True, True, False, Gomme.vide, background))
        self.cases[3].append(Case(3, 1, False, False, True, True, Gomme.gomme, background))
        self.cases[4].append(Case(4, 1, False, True, True, True, Gomme.vide, background))
        self.cases[5].append(Case(5, 1, False, False, True, True, Gomme.gomme, background))
        self.cases[6].append(Case(6, 1, True, True, False, True, Gomme.vide, background))
        for x in range(7, 11):
            self.cases[x].append(Case(x, 1, True, True, False, False, Gomme.vide, background))
        self.cases[11].append(Case(11, 1, True, True, True, False, Gomme.vide, background))
        self.cases[12].append(Case(12, 1, False, False, True, True, Gomme.gomme, background))
        self.cases[13].append(Case(13, 1, False, True, True, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 1, False, False, True, True, Gomme.gomme, background))
        self.cases[15].append(Case(15, 1, True, True, False, True, Gomme.vide, background))
        self.cases[16].append(Case(16, 1, True, False, True, False, Gomme.vide, background))
        self.cases[17].append(Case(17, 1, False, False, True, True, Gomme.gomme, background))

        # ligne 3
        self.cases[0].append(Case(0, 2, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 2, False, False, True, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 2, True, False, False, True, Gomme.gomme, background))

        self.cases[3].append(Case(3, 2, False, True, False, False, Gomme.gomme, background))
        self.cases[4].append(Case(4, 2, True, True, False, False, Gomme.gomme, background))

        self.cases[5].append(Case(5, 2, False, False, False, False, Gomme.gomme, background))
        for x in range(6, 12):
            self.cases[x].append(Case(x, 2, True, True, False, False, Gomme.gomme, background))
        self.cases[12].append(Case(12, 2, False, False, False, False, Gomme.gomme, background))

        self.cases[13].append(Case(13, 2, True, True, False, False, Gomme.gomme, background))
        self.cases[14].append(Case(14, 2, False, True, False, False, Gomme.gomme, background))

        self.cases[15].append(Case(15, 2, True, False, True, False, Gomme.gomme, background))
        self.cases[16].append(Case(16, 2, False, False, True, True, Gomme.vide, background))
        self.cases[17].append(Case(17, 2, False, False, True, True, Gomme.gomme, background))
        # ligne4
        self.cases[0].append(Case(0, 3, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 3, False, True, True, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 3, False, False, True, True, Gomme.gomme, background))
        self.cases[3].append(Case(3, 3, True, True, False, True, Gomme.vide, background))
        self.cases[4].append(Case(4, 3, True, True, True, False, Gomme.vide, background))
        self.cases[5].append(Case(5, 3, False, False, True, True, Gomme.gomme, background))
        self.cases[6].append(Case(6, 3, True, False, False, True, Gomme.vide, background))
        self.cases[7].append(Case(7, 3, True, True, True, False, Gomme.vide, background))
        self.cases[8].append(Case(8, 3, False, False, False, True, Gomme.vide, background))
        self.cases[9].append(Case(9, 3, False, False, True, False, Gomme.vide, background))
        self.cases[10].append(Case(10, 3, True, True, False, True, Gomme.vide, background))
        self.cases[11].append(Case(11, 3, True, False, True, False, Gomme.vide, background))
        self.cases[12].append(Case(12, 3, False, False, True, True, Gomme.gomme, background))
        self.cases[13].append(Case(13, 3, True, True, False, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 3, True, True, True, False, Gomme.vide, background))
        self.cases[15].append(Case(15, 3, False, False, True, True, Gomme.gomme, background))
        self.cases[16].append(Case(16, 3, False, True, True, True, Gomme.vide, background))
        self.cases[17].append(Case(17, 3, False, False, True, True, Gomme.gomme, background))
        # ligne5
        self.cases[0].append(Case(0, 4, False, False, False, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 4, True, True, False, False, Gomme.gomme, background))
        self.cases[2].append(Case(2, 4, False, False, False, False, Gomme.gomme, background))
        for x in range(3, 5):
            self.cases[x].append(Case(x, 4, True, True, False, False, Gomme.gomme, background))
        self.cases[5].append(Case(5, 4, False, False, True, False, Gomme.gomme, background))
        self.cases[6].append(Case(6, 4, False, False, True, True, Gomme.vide, background))
        self.cases[7].append(Case(7, 4, True, True, False, True, Gomme.vide, background))
        for x in range(8, 10):
            self.cases[x].append(Case(x, 4, False, True, False, False, Gomme.vide, background))
        self.cases[10].append(Case(10, 4, True, True, True, False, Gomme.vide, background))
        self.cases[11].append(Case(11, 4, False, False, True, True, Gomme.vide, background))
        self.cases[12].append(Case(12, 4, False, False, False, True, Gomme.gomme, background))
        for x in range(13, 15):
            self.cases[x].append(Case(x, 4, True, True, False, False, Gomme.gomme, background))
        self.cases[15].append(Case(15, 4, False, False, False, False, Gomme.gomme, background))
        self.cases[16].append(Case(16, 4, True, True, False, False, Gomme.gomme, background))
        self.cases[17].append(Case(17, 4, False, False, True, False, Gomme.gomme, background))
        # ligne6
        self.cases[0].append(Case(0, 5, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 5, True, False, True, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 5, False, False, True, True, Gomme.gomme, background))
        self.cases[3].append(Case(3, 5, True, True, False, True, Gomme.vide, background))
        self.cases[4].append(Case(4, 5, True, True, True, False, Gomme.vide, background))
        self.cases[5].append(Case(5, 5, False, False, True, True, Gomme.gomme, background))
        self.cases[6].append(Case(6, 5, False, True, False, True, Gomme.vide, background))
        for x in range(7, 11):
            self.cases[x].append(Case(x, 5, True, True, False, False, Gomme.vide, background))
        self.cases[11].append(Case(11, 5, False, True, True, False, Gomme.vide, background))
        self.cases[12].append(Case(12, 5, False, False, True, True, Gomme.gomme, background))
        self.cases[13].append(Case(13, 5, True, True, False, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 5, True, True, True, False, Gomme.vide, background))
        self.cases[15].append(Case(15, 5, False, False, True, True, Gomme.gomme, background))
        self.cases[16].append(Case(16, 5, True, False, True, True, Gomme.vide, background))
        self.cases[17].append(Case(17, 5, False, False, True, True, Gomme.gomme, background))
        # ligne 7
        self.cases[0].append(Case(0, 6, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 6, False, False, True, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 6, False, True, False, True, Gomme.gomme, background))

        self.cases[3].append(Case(3, 6, True, False, False, False, Gomme.gomme, background))
        self.cases[4].append(Case(4, 6, True, True, False, False, Gomme.gomme, background))

        self.cases[5].append(Case(5, 6, False, False, False, False, Gomme.gomme, background))
        for x in range(6, 12):
            self.cases[x].append(Case(x, 6, True, True, False, False, Gomme.gomme, background))
        self.cases[12].append(Case(12, 6, False, False, False, False, Gomme.gomme, background))

        self.cases[13].append(Case(13, 6, True, True, False, False, Gomme.gomme, background))
        self.cases[14].append(Case(14, 6, True, False, False, False, Gomme.gomme, background))

        self.cases[15].append(Case(15, 6, False, True, True, False, Gomme.gomme, background))
        self.cases[16].append(Case(16, 6, False, False, True, True, Gomme.vide, background))
        self.cases[17].append(Case(17, 6, False, False, True, True, Gomme.gomme, background))
        # ligne 8
        self.cases[0].append(Case(0, 7, False, False, True, True, Gomme.gomme, background))
        self.cases[1].append(Case(1, 7, False, True, False, True, Gomme.vide, background))
        self.cases[2].append(Case(2, 7, True, True, True, False, Gomme.vide, background))
        self.cases[3].append(Case(3, 7, False, False, True, True, Gomme.gomme, background))
        self.cases[4].append(Case(4, 7, True, False, True, True, Gomme.vide, background))
        self.cases[5].append(Case(5, 7, False, False, True, True, Gomme.gomme, background))
        self.cases[6].append(Case(6, 7, True, True, False, True, Gomme.vide, background))
        for x in range(7, 11):
            self.cases[x].append(Case(x, 7, True, True, False, False, Gomme.vide, background))
        self.cases[11].append(Case(11, 7, True, True, True, False, Gomme.vide, background))
        self.cases[12].append(Case(12, 7, False, False, True, True, Gomme.gomme, background))
        self.cases[13].append(Case(13, 7, True, False, True, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 7, False, False, True, True, Gomme.gomme, background))
        self.cases[15].append(Case(15, 7, True, True, False, True, Gomme.vide, background))
        self.cases[16].append(Case(16, 7, False, True, True, False, Gomme.vide, background))
        self.cases[17].append(Case(17, 7, False, False, True, True, Gomme.gomme, background))
        # ligne 9
        self.cases[0].append(Case(0, 8, False, True, False, True, Gomme.gomme, background))
        for x in range(1, 3):
            self.cases[x].append(Case(x, 8, True, True, False, False, Gomme.gomme, background))
        self.cases[3].append(Case(3, 8, False, True, True, False, Gomme.gomme, background))
        self.cases[4].append(Case(4, 8, False, False, True, True, Gomme.vide, background))
        self.cases[5].append(Case(5, 8, False, True, False, True, Gomme.gomme, background))
        for x in range(6, 12):
            self.cases[x].append(Case(x, 8, True, True, False, False, Gomme.gomme, background))
        self.cases[12].append(Case(12, 8, False, True, True, False, Gomme.gomme, background))
        self.cases[13].append(Case(13, 8, False, False, True, True, Gomme.vide, background))
        self.cases[14].append(Case(14, 8, False, True, False, True, Gomme.gomme, background))
        for x in range(15, 17):
            self.cases[x].append(Case(x, 8, True, True, False, False, Gomme.gomme, background))
        self.cases[17].append(Case(17, 8, False, True, True, False, Gomme.superGomme, background))
        self.ticks = 1
        self.pacman = PacMan(self.background, self.statusPartie, self.cases)
        self.fantomes = [Fantome(self.background, self.pacman, self.cases) for f in range(1)]
        self.window.bind("<Up>", self.pacman.monter)
        self.window.bind("<Down>", self.pacman.descendre)
        self.window.bind("<Right>", self.pacman.droite)
        self.window.bind("<Left>", self.pacman.gauche)

    def clear(self):
        self.background.delete("all")
        self = self.__init__(self.window, self.background, self.statusPartie)

    def motion(self):
        for f in self.fantomes:
            if self.pacman.ticks != 0:
                f.objectif = Objectif.fuir
                fantomeImg = Image.open("images/voilabis.jpg").resize((int(l / 2), int(l / 2)), resample=0)
                fantomeImg = ImageTk.PhotoImage(fantomeImg)
                f.image = fantomeImg
                f.sprite = f.background.create_image(f.x * l + (3 * e), f.y * l + (3 * e), image=f.image)
                if self.pacman.x == f.x and self.pacman.y == f.y:
                    self.pacman.ticks = 0
                    f.mourir()
            elif f.objectif == Objectif.fuir:
                f.objectif = Objectif.chercher
                fantomeImg = Image.open("images/fantome.jpg").resize((int(l / 2), int(l / 2)), resample=0)
                fantomeImg = ImageTk.PhotoImage(fantomeImg)
                f.image = fantomeImg
                f.sprite = f.background.create_image(f.x * l + (3 * e), f.y * l + (3 * e), image=f.image)
            f.bouger()

        self.ticks += 1
        self.pacman.hasMoved = False
        if self.pacman.ticks != 0:
            self.pacman.ticks -= 1
        if self.statusPartie.get() in [Status.pause.value, Status.perdu.value, Status.gagne.value]:
            if self.statusPartie.get() == Status.gagne.value:
                self.endscreen = self.background.create_image(0, 0, image=self.victoryImg, anchor="nw")
            elif self.statusPartie.get() == Status.perdu.value:
                self.endscreen = self.background.create_image(0, 0, image=self.defeatImg, anchor="nw")
            return False
        self.window.after(500, self.motion)

    def start(self, event):
        if self.statusPartie.get() == Status.pause.value:
            self.statusPartie.set(Status.enCours.value)
            self.motion()
        elif self.statusPartie.get() == Status.enCours.value:
            self.statusPartie.set(Status.pause.value)
        else:
            self.statusPartie.set(Status.pause.value)
            self.clear()
        print(self.statusPartie.get())
