from Constants import e, l
from labyrinthe.Gomme import Gomme
from labyrinthe.Mur import Mur


class Case:
    # constructeur
    def __init__(self, x: int, y: int, haut: bool, bas: bool, droite: bool, gauche: bool, gomme, background):
        self.background = background
        self.x = x # coordonnées case
        self.y = y
        self.haut = haut # murs en haut?
        self.bas = bas
        self.gauche = gauche
        self.droite = droite
        self.gomme = gomme
        if haut:
            Mur(x * l, y * l, (x + 1) * l, y * l + e, self.background)
        if bas:
            Mur(x * l, (y + 1) * l - e, (x + 1) * l, (y + 1) * l, self.background)
        if gauche:
            Mur(x * l, y * l, x * l + e, (y + 1) * l, self.background)
        if droite:
            Mur((x + 1) * l - e, y * l, (x + 1) * l, (y + 1) * l, self.background)
        if gomme == Gomme.gomme:
            self.sprite = self.background.create_oval(self.x * l + l / 2 - 5, self.y * l + l / 2 - 5, self.x * l + l / 2 + 5, self.y * l + l / 2 + 5, fill="yellow")
        if gomme == Gomme.superGomme:
            self.sprite = self.background.create_oval(self.x * l + l / 2 - 10, self.y * l + l / 2 - 10, self.x * l + l / 2 + 10, self.y * l + l / 2 + 10, fill="yellow")
