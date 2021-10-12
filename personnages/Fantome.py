import random
from PIL import ImageTk, Image
from Constants import e, l
from Enumerations import Action, Objectif


class FBlackboard:
    """
    Tableau noir / registre d'informations partagé entre les fantômes.
    """

    def __init__(self):
        self.data = {}
        self.name = 0  # plus tard, des prénoms pour humaniser

    def ecrire_blackboard(self, name, action, objectif, x, y):
        """
        Un fantome possédant un attribut de type FBlackboard peut écrire ses informations dans un registre visible par
        d'autres fantômes possédant le même registre.
        """
        self.data[name] = {
            "action": action,
            "objectif": objectif,
            "x": x,
            "y": y,
        }

    def lire_blackboard(self, name):
        """
        Renvoit les données du blackboard - le fantôme courant
        :param name: nom du fantôme à exclure
        :return: les données du blackboard
        """
        return [self.data[n] for n in self.data if n != name]



class Fantome:
    """
    La classe fantôme représente un agent avec des coordonnées. Le fantome peut tuer PacMan, revivre si PacMan le tue.
    C'est un agent qui obéit à des objectifs et agit (actions) en fonction. Il y a un comportement qui fait que
    le fantome suit PacMan s'il le voit à travers les murs. Il fait le comportement inverse s'il doit le "fuir".
    """

    def __init__(self, background, cases, blackboard: FBlackboard, image, nom):
        self.name = blackboard.name  # associe le nom
        blackboard.name += 1  # incrémente le nom, index nom
        self.background = background
        self.pacman = None
        self.cases = cases
        self.blackboard = blackboard
        self.x = 9
        self.y = 4
        self.action = Action.monter
        self.objectif = Objectif.sortir
        self.img = image
        fantomeImg = Image.open(image).resize((int(l / 2), int(l / 2)), resample=0)
        fantomeImg = ImageTk.PhotoImage(fantomeImg)
        self.image = fantomeImg
        self.sprite = self.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)
        self.nom = nom
        self.arret = False


    def bouger(self):
        while(self.arret):
            continue
        self.blackboard.ecrire_blackboard(self.name, self.action, self.objectif, self.x, self.y)
        if self.objectif == Objectif.chercher:
            self.action = self.chercher()  # cherche pacman
        elif self.objectif == Objectif.sortir:
            self.action = self.sortir()
        elif self.objectif == Objectif.fuir:
            self.action = self.fuir()
        else:
            self.action = self.chercher()
        self.deplacer(self.action)  # effectue le déplacement
        self.tuer()  # essaye de tuer pacman

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
        fantomes = self.blackboard.lire_blackboard(self.name)
        if self.pacman.x == self.x:  # si self.pacman meme colonne que fantome
            if self.pacman.y > self.y:  # si fantome plus haut que self.pacman
                i = self.y
                while i < self.pacman.y and test == False:  # est-ce que ya des murs entre ?
                    if self.cases[self.x][i].bas:
                        test = True  # => oui
                    i += 1
                if not test:
                    i = 0
                    while i < len(fantomes) and test == False:
                        if fantomes[i]["x"] == self.x and fantomes[i]["y"] < self.y:
                            test = True  # => oui
                        i += 1
                    if not test:
                        return Action.descendre  # => non donc on descend
                    r = random.randint(0, 1)
                    if r == 0 and self.action == Action.gauche:
                        r = 1
                    if r == 1 and self.action == Action.droite:
                        r = 0
                    if r == 0 and self.cases[self.x][self.y].droite != True:
                        return Action.droite
                    if r == 0 and self.cases[self.x][self.y].droite == True:
                        if self.cases[self.x][self.y].gauche == True:
                            return Action.descendre
                        return Action.gauche
                    if self.cases[self.x][self.y].gauche != True:
                        return Action.gauche
                    if self.cases[self.x][self.y].droite == True:
                        return Action.descendre
                    return Action.droite
            else:  # sinon fantome plus bas
                i = self.pacman.y
                while i < self.y and test == False:
                    if self.cases[self.x][i].bas:
                        test = True
                    i += 1
                if not test:
                    i = 0
                    while i < len(fantomes) and test == False:
                        if fantomes[i]["x"] == self.x and fantomes[i]["y"] > self.y:
                            test = True  # => oui
                        i += 1
                    if not test:
                        return Action.monter  # => non donc on monte
                    r = random.randint(0, 1)
                    if r == 0 and self.action == Action.gauche:
                        r = 1
                    if r == 1 and self.action == Action.droite:
                        r = 0
                    if r == 0 and self.cases[self.x][self.y].droite != True:
                        return Action.droite
                    if r == 0 and self.cases[self.x][self.y].droite == True:
                        if self.cases[self.x][self.y].gauche == True:
                            return Action.monter
                        return Action.gauche
                    if self.cases[self.x][self.y].gauche != True:
                        return Action.gauche
                    if self.cases[self.x][self.y].droite == True:
                        return Action.monter
                    return Action.droite
        if self.pacman.y == self.y:
            if self.pacman.x > self.x:
                i = self.x
                while i < self.pacman.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    i = 0
                    while i < len(fantomes) and test == False:
                        if fantomes[i]["y"] == self.y and fantomes[i]["x"] < self.x:
                            test = True  # => oui
                        i += 1
                    if not test:
                        return Action.droite  # => non donc on va a droite
                    r = random.randint(0, 1)
                    if r == 0 and self.action == Action.monter:
                        r = 1
                    if r == 1 and self.action == Action.descendre:
                        r = 0
                    if r == 0 and self.cases[self.x][self.y].bas != True:
                        return Action.descendre
                    if r == 0 and self.cases[self.x][self.y].bas == True:
                        if self.cases[self.x][self.y].haut == True:
                            return Action.droite
                        return Action.monter
                    if self.cases[self.x][self.y].haut != True:
                        return Action.monter
                    if self.cases[self.x][self.y].bas == True:
                        return Action.droite
                    return Action.descendre
            else:
                i = self.pacman.x
                while i < self.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if not test:
                    i = 0
                    while i < len(fantomes) and test == False:
                        if fantomes[i]["y"] == self.y and fantomes[i]["x"] < self.x:
                            test = True  # => oui
                        i += 1
                    if not test:
                        return Action.gauche  # => non donc on va a gauche
                    r = random.randint(0, 1)
                    if r == 0 and self.action == Action.monter:
                        r = 1
                    if r == 1 and self.action == Action.descendre:
                        r = 0
                    if r == 0 and self.cases[self.x][self.y].bas != True:
                        return Action.descendre
                    if r == 0 and self.cases[self.x][self.y].bas == True:
                        if self.cases[self.x][self.y].haut == True:
                            return Action.gauche
                        return Action.monter
                    if self.cases[self.x][self.y].haut != True:
                        return Action.monter
                    if self.cases[self.x][self.y].bas == True:
                        return Action.gauche
                    return Action.descendre
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            self.cases[self.x][self.y].haut == True,  # mur == true => true
            self.cases[self.x][self.y].droite == True,
            self.cases[self.x][self.y].gauche == True,
            self.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3)  # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3:  # si mur == true
            r = random.randint(0, 3)  # => relance aléatoire
        return Action(r)

    # mouvement inverse
    def fuir(self):
        test = False
        if self.pacman.x == self.x:  # si self.pacman meme colonne que fantome
            if self.pacman.y > self.y:  # si fantome plus haut que self.pacman
                i = self.y
                while i < self.pacman.y and test == False:  # est-ce que ya des murs entre ?
                    if self.cases[self.x][i].bas:
                        test = True  # => oui
                    i += 1
                if self.cases[self.x][self.y].haut:
                    test = True
                if not test:
                    return Action.monter  # => non donc on descend
            else:  # sinon fantome plus bas
                i = self.pacman.y
                while i < self.y and test == False:
                    if self.cases[self.x][i].bas:
                        test = True
                    i += 1
                if self.cases[self.x][self.y].bas:
                    test = True
                if not test:
                    return Action.descendre  # => donc on monte
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
                    return Action.gauche  # => on va a droite
            else:
                i = self.pacman.x
                while i < self.x and test == False:
                    if self.cases[i][self.y].droite:
                        test = True
                    i += 1
                if self.cases[self.x][self.y].droite:
                    test = True
                if not test:
                    return Action.droite  # => on va a droite
        """
        déplacement aléatoire:
            - si action mémorisé et déplacement possible => la meme action
            - sinon aléatoire
        """
        listeActionsPossibles = [
            self.cases[self.x][self.y].haut == True,  # mur == true => true
            self.cases[self.x][self.y].droite == True,
            self.cases[self.x][self.y].gauche == True,
            self.cases[self.x][self.y].bas == True
        ]
        r = random.randint(0, 3)  # aléatoire
        while listeActionsPossibles[r] or self.action.value + r == 3:  # si mur == true
            r = random.randint(0, 3)  # => relance aléatoire
        return Action(r)

    # objectif: tuer pacman
    def tuer(self):
        if self.objectif == Objectif.chercher:
            if self.pacman.x == self.x and self.pacman.y == self.y:
                self.pacman.mourir()

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

    def mourir(self):
        self.x = 9
        self.y = 4
        self.action = Action.monter
        self.objectif = Objectif.sortir
        fantomeImg = Image.open("images/fantome.jpg").resize((int(l / 2), int(l / 2)), resample=0)
        fantomeImg = ImageTk.PhotoImage(fantomeImg)
        self.image = fantomeImg
        self.sprite = self.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)
