#! python3

import tkinter
from PIL import ImageTk, Image
from enum import Enum
import random

window = tkinter.Tk()

t = 1008 # taille
l = round(1008/18) # case
h = l * 9 # hauteur
e = 10 # epaisseur
FPS = tkinter.IntVar()
FPS.set(1)


window.title("Pac Man")
window.geometry(str(t)+"x"+str(h))
window.resizable(width=False, height=False)

background = tkinter.Canvas(window, width=t, height=t, background="#000", bd=0, highlightthickness=0)
background.pack()

pacmanImg = Image.open("pacman.jpg").resize((int(l/2), int(l/2)), resample=0)
pacmanImg = ImageTk.PhotoImage(pacmanImg)
fantomeImg = Image.open("fantome.jpg").resize((int(l/2), int(l/2)), resample=0)
fantomeImg = ImageTk.PhotoImage(fantomeImg)

class Mur:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        background.create_rectangle(x1, y1, x2, y2, fill="#fff", outline="#fff")

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
            Mur(x*l, y*l, (x+1)*l, y*l+e)
        if bas:
            Mur(x*l, (y+1)*l-e, (x+1)*l, (y+1)*l)
        if gauche:
            Mur(x*l, y*l, x*l+e, (y+1)*l)
        if droite:
            Mur((x+1)*l-e, y*l, (x+1)*l, (y+1)*l)
        if gomme:
            self.sprite = background.create_oval(self.x * l + l / 2 - 5, self.y * l + l / 2 - 5, self.x * l + l / 2 + 5, self.y * l + l / 2 + 5, fill="yellow")

"""
La classe pacman ......
"""
class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pacmanImg
        self.action = Action.monter
        self.sprite = background.create_image(self.x*l+(3*e), self.y*l+(3*e), image=self.image)
        self.nb_gomme = 99

    def goUp(self, event):
        if not Partie.cases[self.x][self.y].haut:
            self.y -= 1
            background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    statusPartie.set(Status.gagne.value)

    def goDown(self, event):
        if not Partie.cases[self.x][self.y].bas:
            self.y += 1
            background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    statusPartie.set(Status.gagne.value)

    def goRight(self, event):
        if not Partie.cases[self.x][self.y].droite:
            self.x += 1
            background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    statusPartie.set(Status.gagne.value)

    def goLeft(self, event):
        if not Partie.cases[self.x][self.y].gauche:
            self.x -= 1
            background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))
            if Partie.cases[self.x][self.y].gomme:
                Partie.cases[self.x][self.y].gomme = False
                background.delete(Partie.cases[self.x][self.y].sprite)
                self.nb_gomme-=1
                if self.nb_gomme == 0:
                    statusPartie.set(Status.gagne.value)

    def mourrir(self):
        background.delete(self.sprite)
        statusPartie.set(Status.perdu.value)

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
        self.sprite = background.create_image(self.x*l+(3*e), self.y*l+(3*e), image=self.image)

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
        background.coords(self.sprite, self.x*l+(3*e), self.y*l+(3*e))

"""
Énumération des actions de l'agent
"""
class Action(Enum):
    monter = 0
    descendre = 1
    droite = 2
    gauche = 3

"""
Énumération des objectifs de l'agent
"""
class Objectif(Enum):
    chercher = 0
    fuir = 1
    tuer = 2

"""
Object statique représentant une partie.
"""
class Partie(object):
    cases = []
    pacman = None
    fantomes = []
    ticks = 1

    @staticmethod
    def initialize():
        # Labyrinthe
        Partie.cases = []
        for x in range(0, 18):
            Partie.cases.append([])
        ##ligne 1
        Partie.cases[0].append(Case(0, 0, True, False, False, True, False))
        for x in range(1, 3):
            Partie.cases[x].append(Case(x, 0, True, True, False, False, True))
        Partie.cases[3].append(Case(3, 0, True, False, True, False, True))
        Partie.cases[4].append(Case(4, 0, False, False, True, True, False))
        Partie.cases[5].append(Case(5, 0, True, False, False, True, True))
        for x in range(6, 12):
            Partie.cases[x].append(Case(x, 0, True, True, False, False, True))
        Partie.cases[12].append(Case(12, 0, True, False, True, False, True))
        Partie.cases[13].append(Case(13, 0, False, False, True, True, False))
        Partie.cases[14].append(Case(14, 0, True, False, False, True, True))
        for x in range(15, 17):
            Partie.cases[x].append(Case(x, 0, True, True, False, False, True))
        Partie.cases[17].append(Case(17, 0, True, False, True, False, True))
        ##ligne 2
        Partie.cases[0].append(Case(0, 1, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 1, True, False, False, True, False))
        Partie.cases[2].append(Case(2, 1, True, True, True, False, False))
        Partie.cases[3].append(Case(3, 1, False, False, True, True, True))
        Partie.cases[4].append(Case(4, 1, False, True, True, True, False))
        Partie.cases[5].append(Case(5, 1, False, False, True, True, True))
        Partie.cases[6].append(Case(6, 1, True, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(Case(x, 1, True, True, False, False, False))
        Partie.cases[11].append(Case(11, 1, True, True, True, False, False))
        Partie.cases[12].append(Case(12, 1, False, False, True, True, True))
        Partie.cases[13].append(Case(13, 1, False, True, True, True, False))
        Partie.cases[14].append(Case(14, 1, False, False, True, True, True))
        Partie.cases[15].append(Case(15, 1, True, True, False, True, False))
        Partie.cases[16].append(Case(16, 1, True, False, True, False, False))
        Partie.cases[17].append(Case(17, 1, False, False, True, True, True))

        ##ligne 3
        Partie.cases[0].append(Case(0, 2, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 2, False, False, True, True, False))
        Partie.cases[2].append(Case(2, 2, True, False, False, True, True))

        Partie.cases[3].append(Case(3, 2, False, True, False, False, True))
        Partie.cases[4].append(Case(4, 2, True, True, False, False, True))

        Partie.cases[5].append(Case(5, 2, False, False, False, False, True))
        for x in range(6, 12):
            Partie.cases[x].append(Case(x, 2, True, True, False, False, True))
        Partie.cases[12].append(Case(12, 2, False, False, False, False, True))

        Partie.cases[13].append(Case(13, 2, True, True, False, False, True))
        Partie.cases[14].append(Case(14, 2, False, True, False, False, True))

        Partie.cases[15].append(Case(15, 2, True, False, True, False, True))
        Partie.cases[16].append(Case(16, 2, False, False, True, True, False))
        Partie.cases[17].append(Case(17, 2, False, False, True, True, True))
        ##ligne4
        Partie.cases[0].append(Case(0, 3, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 3, False, True, True, True, False))
        Partie.cases[2].append(Case(2, 3, False, False, True, True, True))
        Partie.cases[3].append(Case(3, 3, True, True, False, True, False))
        Partie.cases[4].append(Case(4, 3, True, True, True, False, False))
        Partie.cases[5].append(Case(5, 3, False, False, True, True, True))
        Partie.cases[6].append(Case(6, 3, True, False, False, True, False))
        Partie.cases[7].append(Case(7, 3, True, True, True, False, False))
        Partie.cases[8].append(Case(8, 3, False, False, False, True, False))
        Partie.cases[9].append(Case(9, 3, False, False, True, False, False))
        Partie.cases[10].append(Case(10, 3, True, True, False, True, False))
        Partie.cases[11].append(Case(11, 3, True, False, True, False, False))
        Partie.cases[12].append(Case(12, 3, False, False, True, True, True))
        Partie.cases[13].append(Case(13, 3, True, True, False, True, False))
        Partie.cases[14].append(Case(14, 3, True, True, True, False, False))
        Partie.cases[15].append(Case(15, 3, False, False, True, True, True))
        Partie.cases[16].append(Case(16, 3, False, True, True, True, False))
        Partie.cases[17].append(Case(17, 3, False, False, True, True, True))
        ##ligne5
        Partie.cases[0].append(Case(0, 4, False, False, False, True, True))
        Partie.cases[1].append(Case(1, 4, True, True, False, False, True))
        Partie.cases[2].append(Case(2, 4, False, False, False, False, True))
        for x in range(3, 5):
            Partie.cases[x].append(Case(x, 4, True, True, False, False, True))
        Partie.cases[5].append(Case(5, 4, False, False, True, False, True))
        Partie.cases[6].append(Case(6, 4, False, False, True, True, False))
        Partie.cases[7].append(Case(7, 4, True, True, False, True, False))
        for x in range(8, 10):
            Partie.cases[x].append(Case(x, 4, False, True, False, False, False))
        Partie.cases[10].append(Case(10, 4, True, True, True, False, False))
        Partie.cases[11].append(Case(11, 4, False, False, True, True, False))
        Partie.cases[12].append(Case(12, 4, False, False, False, True, True))
        for x in range(13, 15):
            Partie.cases[x].append(Case(x, 4, True, True, False, False, True))
        Partie.cases[15].append(Case(15, 4, False, False, False, False, True))
        Partie.cases[16].append(Case(16, 4, True, True, False, False, True))
        Partie.cases[17].append(Case(17, 4, False, False, True, False, True))
        ##ligne6
        Partie.cases[0].append(Case(0, 5, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 5, True, False, True, True, False))
        Partie.cases[2].append(Case(2, 5, False, False, True, True, True))
        Partie.cases[3].append(Case(3, 5, True, True, False, True, False))
        Partie.cases[4].append(Case(4, 5, True, True, True, False, False))
        Partie.cases[5].append(Case(5, 5, False, False, True, True, True))
        Partie.cases[6].append(Case(6, 5, False, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(Case(x, 5, True, True, False, False, False))
        Partie.cases[11].append(Case(11, 5, False, True, True, False, False))
        Partie.cases[12].append(Case(12, 5, False, False, True, True, True))
        Partie.cases[13].append(Case(13, 5, True, True, False, True, False))
        Partie.cases[14].append(Case(14, 5, True, True, True, False, False))
        Partie.cases[15].append(Case(15, 5, False, False, True, True, True))
        Partie.cases[16].append(Case(16, 5, True, False, True, True, False))
        Partie.cases[17].append(Case(17, 5, False, False, True, True, True))
        ##ligne 7
        Partie.cases[0].append(Case(0, 6, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 6, False, False, True, True, False))
        Partie.cases[2].append(Case(2, 6, False, True, False, True, True))

        Partie.cases[3].append(Case(3, 6, True, False, False, False, True))
        Partie.cases[4].append(Case(4, 6, True, True, False, False, True))

        Partie.cases[5].append(Case(5, 6, False, False, False, False, True))
        for x in range(6, 12):
            Partie.cases[x].append(Case(x, 6, True, True, False, False, True))
        Partie.cases[12].append(Case(12, 6, False, False, False, False, True))

        Partie.cases[13].append(Case(13, 6, True, True, False, False, True))
        Partie.cases[14].append(Case(14, 6, True, False, False, False, True))

        Partie.cases[15].append(Case(15, 6, False, True, True, False, True))
        Partie.cases[16].append(Case(16, 6, False, False, True, True, False))
        Partie.cases[17].append(Case(17, 6, False, False, True, True, True))
        ##ligne 8
        Partie.cases[0].append(Case(0, 7, False, False, True, True, True))
        Partie.cases[1].append(Case(1, 7, False, True, False, True, False))
        Partie.cases[2].append(Case(2, 7, True, True, True, False, False))
        Partie.cases[3].append(Case(3, 7, False, False, True, True, True))
        Partie.cases[4].append(Case(4, 7, True, False, True, True, False))
        Partie.cases[5].append(Case(5, 7, False, False, True, True, True))
        Partie.cases[6].append(Case(6, 7, True, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(Case(x, 7, True, True, False, False, False))
        Partie.cases[11].append(Case(11, 7, True, True, True, False, False))
        Partie.cases[12].append(Case(12, 7, False, False, True, True, True))
        Partie.cases[13].append(Case(13, 7, True, False, True, True, False))
        Partie.cases[14].append(Case(14, 7, False, False, True, True, True))
        Partie.cases[15].append(Case(15, 7, True, True, False, True, False))
        Partie.cases[16].append(Case(16, 7, False, True, True, False, False))
        Partie.cases[17].append(Case(17, 7, False, False, True, True, True))
        ##ligne 9
        Partie.cases[0].append(Case(0, 8, False, True, False, True, True))
        for x in range(1, 3):
            Partie.cases[x].append(Case(x, 8, True, True, False, False, True))
        Partie.cases[3].append(Case(3, 8, False, True, True, False, True))
        Partie.cases[4].append(Case(4, 8, False, False, True, True, False))
        Partie.cases[5].append(Case(5, 8, False, True, False, True, True))
        for x in range(6, 12):
            Partie.cases[x].append(Case(x, 8, True, True, False, False, True))
        Partie.cases[12].append(Case(12, 8, False, True, True, False, True))
        Partie.cases[13].append(Case(13, 8, False, False, True, True, False))
        Partie.cases[14].append(Case(14, 8, False, True, False, True, True))
        for x in range(15, 17):
            Partie.cases[x].append(Case(x, 8, True, True, False, False, True))
        Partie.cases[17].append(Case(17, 8, False, True, True, False, True))
        Partie.ticks = 1
        Partie.pacman = PacMan()
        Partie.fantomes = [Fantome() for f in range(1)]
        window.bind("<Up>", Partie.pacman.goUp)
        window.bind("<Down>", Partie.pacman.goDown)
        window.bind("<Right>", Partie.pacman.goRight)
        window.bind("<Left>", Partie.pacman.goLeft)

    @staticmethod
    def clear():
        for x in Partie.cases:
            for y in x:
                if y.gomme:
                    background.delete(y.sprite)
        background.delete(Partie.pacman.sprite)
        [background.delete(f.sprite) for f in Partie.fantomes]

    @staticmethod
    def motion():
        for f in Partie.fantomes:
            f.bouger()
        Partie.ticks += 1
        if statusPartie.get() in [Status.pause.value, Status.perdu.value, Status.gagne.value]:
            return False
        window.after(int(1000/FPS.get()), Partie.motion)

    @staticmethod
    def start():
        if statusPartie.get() == Status.pause.value:
            statusPartie.set(Status.enCours.value)
            Partie.motion()
        elif statusPartie.get() == Status.enCours.value:
            statusPartie.set(Status.pause.value)
        else:
            statusPartie.set(Status.enCours.value)
            Partie.clear()
            Partie.initialize()

controls = tkinter.Toplevel()

controls.resizable(width = False, height = False)
controls.title("Contrôles")
controls.geometry("200x350")
#controls.attributes("-toolwindow", 1)	# Enlever le bouton pour redimensionner la fenetre

statusPartie = tkinter.StringVar()
statusPartie.set("pause")

Partie.initialize()

class Status(Enum):
    pause = "pause"
    enCours = "en cours"
    perdu = "perdu !"
    gagne = "gagné !"

labelPartie = tkinter.Label(controls, text="Partie: " + statusPartie.get())
buttonPartie = tkinter.Button(controls, command=Partie.start)
labelVitesse = tkinter.Label(controls, text="Vitesse:") # modifier vitesse
scaleVitesse = tkinter.Scale(controls, orient=tkinter.HORIZONTAL, from_=1, to=60, length=180, variable=FPS, cursor='sb_h_double_arrow') # Curseur pour modifier les FPS

labelPartie.pack()
buttonPartie.pack()
labelVitesse.pack()
scaleVitesse.pack()

window.mainloop()
