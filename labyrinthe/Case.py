import Constants
import labyrinthe.Mur
import App


class Case:
    # constructeur
    def __init__(self, x: int, y: int, haut: bool, bas: bool, droite: bool, gauche: bool, gomme: bool = True):
        self.x = x # coordonnées case
        self.y = y
        self.haut = haut # murs en haut?
        self.bas = bas
        self.gauche = gauche
        self.droite = droite
        self.gomme = gomme
        if haut:
            labyrinthe.Mur.Mur(x * Constants.l, y * Constants.l, (x + 1) * Constants.l, y * Constants.l + Constants.e)
        if bas:
            labyrinthe.Mur.Mur(x * Constants.l, (y + 1) * Constants.l - Constants.e, (x + 1) * Constants.l, (y + 1) * Constants.l)
        if gauche:
            labyrinthe.Mur.Mur(x * Constants.l, y * Constants.l, x * Constants.l + Constants.e, (y + 1) * Constants.l)
        if droite:
            labyrinthe.Mur.Mur((x + 1) * Constants.l - Constants.e, y * Constants.l, (x + 1) * Constants.l, (y + 1) * Constants.l)
        if gomme:
            self.sprite = App.App.background.create_oval(self.x * Constants.l + Constants.l / 2 - 5, self.y * Constants.l + Constants.l / 2 - 5, self.x * Constants.l + Constants.l / 2 + 5, self.y * Constants.l + Constants.l / 2 + 5, fill="yellow")