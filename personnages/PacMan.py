from PIL import Image, ImageTk
import Partie
import Constants
import Enumerations
import App


"""
La classe pacman ......
"""
class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        pacmanImg = Image.open("images/pacman.jpg").resize((int(Constants.l / 2), int(Constants.l / 2)), resample=0)
        pacmanImg = ImageTk.PhotoImage(pacmanImg)
        self.image = pacmanImg
        self.action = Enumerations.Action.monter
        self.sprite = App.App.background.create_image(self.x * Constants.l + (3 * Constants.e), self.y * Constants.l + (3 * Constants.e), image=self.image)
        self.nb_gomme = 99

    def goUp(self, event):
        if not Partie.Partie.cases[self.x][self.y].haut:
            self.y -= 1
            App.App.background.coords(self.sprite, self.x * Constants.l + (3 * Constants.e), self.y * Constants.l + (3 * Constants.e))
            if Partie.Partie.cases[self.x][self.y].gomme:
                Partie.Partie.cases[self.x][self.y].gomme = False
                App.App.background.delete(Partie.Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.App.statusPartie.set(App.Status.gagne.value)

    def goDown(self, event):
        if not Partie.Partie.cases[self.x][self.y].bas:
            self.y += 1
            App.App.background.coords(self.sprite, self.x * Constants.l + (3 * Constants.e), self.y * Constants.l + (3 * Constants.e))
            if Partie.Partie.cases[self.x][self.y].gomme:
                Partie.Partie.cases[self.x][self.y].gomme = False
                App.App.background.delete(Partie.Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.App.statusPartie.set(App.Status.gagne.value)

    def goRight(self, event):
        if not Partie.Partie.cases[self.x][self.y].droite:
            self.x += 1
            App.App.background.coords(self.sprite, self.x * Constants.l + (3 * Constants.e), self.y * Constants.l + (3 * Constants.e))
            if Partie.Partie.cases[self.x][self.y].gomme:
                Partie.Partie.cases[self.x][self.y].gomme = False
                App.App.background.delete(Partie.Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.App.statusPartie.set(App.Status.gagne.value)

    def goLeft(self, event):
        if not Partie.Partie.cases[self.x][self.y].gauche:
            self.x -= 1
            App.App.background.coords(self.sprite, self.x * Constants.l + (3 * Constants.e), self.y * Constants.l + (3 * Constants.e))
            if Partie.Partie.cases[self.x][self.y].gomme:
                Partie.Partie.cases[self.x][self.y].gomme = False
                App.App.background.delete(Partie.Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    App.App.statusPartie.set(App.Status.gagne.value)

    def mourrir(self):
        App.App.background.delete(self.sprite)
        App.App.statusPartie.set(App.Status.perdu.value)