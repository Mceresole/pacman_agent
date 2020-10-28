from PIL import Image, ImageTk
import Partie
from Constants import l, e
from Enumerations import Action, Status
from App import *

pacmanImg = Image.open("images/pacman.jpg").resize((int(l/2), int(l/2)), resample=0)
pacmanImg = ImageTk.PhotoImage(pacmanImg)

"""
La classe pacman ......
"""
class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pacmanImg
        self.action = Action.monter
        self.sprite = App.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)
        self.nb_gomme = 99

    def goUp(self, event):
        if not Partie.cases[self.x][self.y].haut:
            self.y -= 1
            App.background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                App.background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.statusPartie.set(Status.gagne.value)

    def goDown(self, event):
        if not Partie.cases[self.x][self.y].bas:
            self.y += 1
            App.background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                App.background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.statusPartie.set(Status.gagne.value)

    def goRight(self, event):
        if not Partie.cases[self.x][self.y].droite:
            self.x += 1
            App.background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                App.background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.statusPartie.set(Status.gagne.value)

    def goLeft(self, event):
        if not Partie.cases[self.x][self.y].gauche:
            self.x -= 1
            App.background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                App.background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.statusPartie.set(Status.gagne.value)

    def mourrir(self):
        App.background.delete(self.sprite)
        App.statusPartie.set(Status.perdu.value)