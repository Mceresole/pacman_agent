from App import *
from Enumerations import Status
import labyrinthe.Case
import personnages.PacMan, personnages.Fantome


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
        Partie.cases[0].append(labyrinthe.Case.Case(0, 0, True, False, False, True, False))
        for x in range(1, 3):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 0, True, True, False, False, True))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 0, True, False, True, False, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 0, False, False, True, True, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 0, True, False, False, True, True))
        for x in range(6, 12):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 0, True, True, False, False, True))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 0, True, False, True, False, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 0, False, False, True, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 0, True, False, False, True, True))
        for x in range(15, 17):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 0, True, True, False, False, True))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 0, True, False, True, False, True))
        ##ligne 2
        Partie.cases[0].append(labyrinthe.Case.Case(0, 1, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 1, True, False, False, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 1, True, True, True, False, False))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 1, False, False, True, True, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 1, False, True, True, True, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 1, False, False, True, True, True))
        Partie.cases[6].append(labyrinthe.Case.Case(6, 1, True, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 1, True, True, False, False, False))
        Partie.cases[11].append(labyrinthe.Case.Case(11, 1, True, True, True, False, False))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 1, False, False, True, True, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 1, False, True, True, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 1, False, False, True, True, True))
        Partie.cases[15].append(labyrinthe.Case.Case(15, 1, True, True, False, True, False))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 1, True, False, True, False, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 1, False, False, True, True, True))

        ##ligne 3
        Partie.cases[0].append(labyrinthe.Case.Case(0, 2, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 2, False, False, True, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 2, True, False, False, True, True))

        Partie.cases[3].append(labyrinthe.Case.Case(3, 2, False, True, False, False, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 2, True, True, False, False, True))

        Partie.cases[5].append(labyrinthe.Case.Case(5, 2, False, False, False, False, True))
        for x in range(6, 12):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 2, True, True, False, False, True))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 2, False, False, False, False, True))

        Partie.cases[13].append(labyrinthe.Case.Case(13, 2, True, True, False, False, True))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 2, False, True, False, False, True))

        Partie.cases[15].append(labyrinthe.Case.Case(15, 2, True, False, True, False, True))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 2, False, False, True, True, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 2, False, False, True, True, True))
        ##ligne4
        Partie.cases[0].append(labyrinthe.Case.Case(0, 3, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 3, False, True, True, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 3, False, False, True, True, True))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 3, True, True, False, True, False))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 3, True, True, True, False, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 3, False, False, True, True, True))
        Partie.cases[6].append(labyrinthe.Case.Case(6, 3, True, False, False, True, False))
        Partie.cases[7].append(labyrinthe.Case.Case(7, 3, True, True, True, False, False))
        Partie.cases[8].append(labyrinthe.Case.Case(8, 3, False, False, False, True, False))
        Partie.cases[9].append(labyrinthe.Case.Case(9, 3, False, False, True, False, False))
        Partie.cases[10].append(labyrinthe.Case.Case(10, 3, True, True, False, True, False))
        Partie.cases[11].append(labyrinthe.Case.Case(11, 3, True, False, True, False, False))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 3, False, False, True, True, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 3, True, True, False, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 3, True, True, True, False, False))
        Partie.cases[15].append(labyrinthe.Case.Case(15, 3, False, False, True, True, True))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 3, False, True, True, True, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 3, False, False, True, True, True))
        ##ligne5
        Partie.cases[0].append(labyrinthe.Case.Case(0, 4, False, False, False, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 4, True, True, False, False, True))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 4, False, False, False, False, True))
        for x in range(3, 5):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 4, True, True, False, False, True))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 4, False, False, True, False, True))
        Partie.cases[6].append(labyrinthe.Case.Case(6, 4, False, False, True, True, False))
        Partie.cases[7].append(labyrinthe.Case.Case(7, 4, True, True, False, True, False))
        for x in range(8, 10):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 4, False, True, False, False, False))
        Partie.cases[10].append(labyrinthe.Case.Case(10, 4, True, True, True, False, False))
        Partie.cases[11].append(labyrinthe.Case.Case(11, 4, False, False, True, True, False))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 4, False, False, False, True, True))
        for x in range(13, 15):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 4, True, True, False, False, True))
        Partie.cases[15].append(labyrinthe.Case.Case(15, 4, False, False, False, False, True))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 4, True, True, False, False, True))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 4, False, False, True, False, True))
        ##ligne6
        Partie.cases[0].append(labyrinthe.Case.Case(0, 5, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 5, True, False, True, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 5, False, False, True, True, True))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 5, True, True, False, True, False))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 5, True, True, True, False, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 5, False, False, True, True, True))
        Partie.cases[6].append(labyrinthe.Case.Case(6, 5, False, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 5, True, True, False, False, False))
        Partie.cases[11].append(labyrinthe.Case.Case(11, 5, False, True, True, False, False))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 5, False, False, True, True, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 5, True, True, False, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 5, True, True, True, False, False))
        Partie.cases[15].append(labyrinthe.Case.Case(15, 5, False, False, True, True, True))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 5, True, False, True, True, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 5, False, False, True, True, True))
        ##ligne 7
        Partie.cases[0].append(labyrinthe.Case.Case(0, 6, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 6, False, False, True, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 6, False, True, False, True, True))

        Partie.cases[3].append(labyrinthe.Case.Case(3, 6, True, False, False, False, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 6, True, True, False, False, True))

        Partie.cases[5].append(labyrinthe.Case.Case(5, 6, False, False, False, False, True))
        for x in range(6, 12):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 6, True, True, False, False, True))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 6, False, False, False, False, True))

        Partie.cases[13].append(labyrinthe.Case.Case(13, 6, True, True, False, False, True))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 6, True, False, False, False, True))

        Partie.cases[15].append(labyrinthe.Case.Case(15, 6, False, True, True, False, True))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 6, False, False, True, True, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 6, False, False, True, True, True))
        ##ligne 8
        Partie.cases[0].append(labyrinthe.Case.Case(0, 7, False, False, True, True, True))
        Partie.cases[1].append(labyrinthe.Case.Case(1, 7, False, True, False, True, False))
        Partie.cases[2].append(labyrinthe.Case.Case(2, 7, True, True, True, False, False))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 7, False, False, True, True, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 7, True, False, True, True, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 7, False, False, True, True, True))
        Partie.cases[6].append(labyrinthe.Case.Case(6, 7, True, True, False, True, False))
        for x in range(7, 11):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 7, True, True, False, False, False))
        Partie.cases[11].append(labyrinthe.Case.Case(11, 7, True, True, True, False, False))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 7, False, False, True, True, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 7, True, False, True, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 7, False, False, True, True, True))
        Partie.cases[15].append(labyrinthe.Case.Case(15, 7, True, True, False, True, False))
        Partie.cases[16].append(labyrinthe.Case.Case(16, 7, False, True, True, False, False))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 7, False, False, True, True, True))
        ##ligne 9
        Partie.cases[0].append(labyrinthe.Case.Case(0, 8, False, True, False, True, True))
        for x in range(1, 3):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 8, True, True, False, False, True))
        Partie.cases[3].append(labyrinthe.Case.Case(3, 8, False, True, True, False, True))
        Partie.cases[4].append(labyrinthe.Case.Case(4, 8, False, False, True, True, False))
        Partie.cases[5].append(labyrinthe.Case.Case(5, 8, False, True, False, True, True))
        for x in range(6, 12):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 8, True, True, False, False, True))
        Partie.cases[12].append(labyrinthe.Case.Case(12, 8, False, True, True, False, True))
        Partie.cases[13].append(labyrinthe.Case.Case(13, 8, False, False, True, True, False))
        Partie.cases[14].append(labyrinthe.Case.Case(14, 8, False, True, False, True, True))
        for x in range(15, 17):
            Partie.cases[x].append(labyrinthe.Case.Case(x, 8, True, True, False, False, True))
        Partie.cases[17].append(labyrinthe.Case.Case(17, 8, False, True, True, False, True))
        Partie.ticks = 1
        Partie.pacman = personnages.PacMan.PacMan()
        Partie.fantomes = [personnages.Fantome() for f in range(1)]
        App.window.bind("<Up>", Partie.pacman.goUp)
        App.window.bind("<Down>", Partie.pacman.goDown)
        App.window.bind("<Right>", Partie.pacman.goRight)
        App.window.bind("<Left>", Partie.pacman.goLeft)

    @staticmethod
    def clear():
        for x in Partie.cases:
            for y in x:
                if y.gomme:
                    App.background.delete(y.sprite)
        App.background.delete(Partie.pacman.sprite)
        [App.background.delete(f.sprite) for f in Partie.fantomes]

    @staticmethod
    def motion():
        for f in Partie.fantomes:
            f.bouger()
        Partie.ticks += 1
        if App.statusPartie.get() in [Status.pause.value, Status.perdu.value, Status.gagne.value]:
            App.labelPartie.set(App.statusPartie.get())
            return False
        App.window.after(int(1000 / App.FPS.get()), Partie.motion)

    @staticmethod
    def start():
        if App.statusPartie.get() == Status.pause.value:
            App.statusPartie.set(Status.enCours.value)
            Partie.motion()
        elif App.statusPartie.get() == Status.enCours.value:
            App.statusPartie.set(Status.pause.value)
        else:
            App.statusPartie.set(Status.pause.value)
            Partie.clear()
            Partie.initialize()
        App.labelPartie.set(App.statusPartie.get())