import random
from PIL import Image, ImageTk
from Constants import e, l
from Enumerations import Status, Action, ObjectifPac
from labyrinthe.Gomme import Gomme



class PacMan:
    """
    La classe PacMan. Elle permet de déplacer le héros, manger les gommes, les fantomes si il a mangé
    une super gomme...
    """
    def __init__(self, background, statusPartie, cases, fantomes):
        self.background = background
        self.statusPartie = statusPartie
        self.cases = cases
        self.fantomes = fantomes
        self.x = 0
        self.y = 0
        self.objectif = ObjectifPac.chercher
        pacmanImg = Image.open("images/pacman.jpg").resize((int(l / 2), int(l / 2)), resample=0)
        pacmanImg = ImageTk.PhotoImage(pacmanImg)
        self.image = pacmanImg
        self.action = Action.droite
        self.sprite = self.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)
        self.nb_gomme = 99
        self.ticks = 0
        self.hasMoved = 0
        self.arret = False


    def bouger(self):
        #self.blackboard.ecrire_blackboard(self.name, self.action, self.objectif, self.x, self.y)
        if self.objectif == ObjectifPac.chercher:
            self.action = self.chercher()  # cherche pacman
        elif self.objectif == ObjectifPac.attaquer:
            self.action = self.attaquer()
        else:
            self.action = self.chercher()
        self.deplacer(self.action)  # effectue le déplacement
        if self.objectif == ObjectifPac.chercher:
            for i in range (len(self.fantomes)):
                if self.fantomes[i].x == self.x and self.fantomes[i].y == self.y:
                    self.mourir()
        elif self.objectif == ObjectifPac.attaquer:
            self.tuer()

    
    # objectif: chercher pacman
    def chercher(self):
        test = False
        gommeH = False
        gommeB = False
        gommeG = False
        gommeD = False
        if self.x > 0:
            if self.cases[self.x-1][self.y].gomme in [Gomme.gomme, Gomme.superGomme] and not self.cases[self.x][self.y].gauche:
                gommeG = True
        if self.x < 17:
            if self.cases[self.x+1][self.y].gomme in [Gomme.gomme, Gomme.superGomme] and not self.cases[self.x][self.y].droite:
                gommeD = True
        if self.y > 0:
            if self.cases[self.x][self.y-1].gomme in [Gomme.gomme, Gomme.superGomme] and not self.cases[self.x][self.y].haut:
                gommeH = True
        if self.y < 8:
            if self.cases[self.x][self.y+1].gomme in [Gomme.gomme, Gomme.superGomme]and not self.cases[self.x][self.y].bas:
                gommeB = True

        #choisi une action au hasard parmi celle possible puis regarde si un fantome se trouve sur la ligne ou la colonne concerné
        #   si c'est le cas, change d'action, jusqu'à ce que plus aucune soit possible
        while gommeB or gommeH or gommeG or gommeD:
            listeActionsPossibles = [
                gommeG == True,  # mur == true => true
                gommeD == True,
                gommeH == True,
                gommeB == True
            ]
            r = random.randint(0, 3)  # aléatoire
            while not listeActionsPossibles[r]:  # si mur == true
                r = random.randint(0, 3)  # => relance aléatoire

            if r == 0: # on veut aller à gauche
                for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                    if self.fantomes[i].y == self.y:
                        if self.fantomes[i].x < self.x:
                            j = self.x
                            t = False
                            while j > self.fantomes[i].x and t == False:
                                if self.cases[j][self.y].gauche:
                                    t = True
                                j -= 1
                            if not t:
                                gommeG = False
                if gommeG:
                   return Action.gauche          
            elif r == 1:
                for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                    if self.fantomes[i].y == self.y:
                        if self.fantomes[i].x > self.x:
                            j = self.x
                            t = False
                            while j < self.fantomes[i].x and t == False:
                                if self.cases[j][self.y].droite:
                                    t = True
                                j += 1
                            if not t:
                                gommeD = False
                if gommeD:
                   return Action.droite     
            elif r == 2:
                for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                    if self.fantomes[i].x == self.x:
                        if self.fantomes[i].y < self.y:
                            j = self.y
                            t = False
                            while j > self.fantomes[i].y and t == False:
                                if self.cases[self.x][j].haut:
                                    t = True
                                j -= 1
                            if not t:
                                gommeH = False
                if gommeH:
                   return Action.monter
            else :
                for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                    if self.fantomes[i].x == self.x:
                        if self.fantomes[i].y > self.y:
                            j = self.y
                            t = False
                            while j < self.fantomes[i].y and t == False:
                                if self.cases[self.x][j].bas:
                                    t = True
                                j += 1
                            if not t:
                                gommeB = False
                if gommeB:
                   return Action.descendre
        
        #aucune action n'est possible (gomme en vue sans fantome dans la direction) donc pacman se tourne vers le joueur
        for i in range(len(self.fantomes)):
            self.fantomes[i].arret = True
        self.arret = True
        list = []
        list.append("a")
        c = "      "
        if not self.cases[self.x][self.y].gauche:
            c += " gauche (q)        "
            list.append("q")
        if not self.cases[self.x][self.y].droite:
            c += " droite (d)        "
            list.append("d")
        if not self.cases[self.x][self.y].haut:
            c += " haut (z)        "
            list.append("z")
        if not self.cases[self.x][self.y].bas:
            c += " bas (s)        "
            list.append("s")
        c += " suicide (a)"
    
        print("Je suis bloqué, où dois-je aller ?")
        print(c)

        c = input()
        while c not in list :#["a","q","d","s","z"]:
            print("Je ne comprends pas. Où dois-je aller ?")
            c = "      "
            if not self.cases[self.x][self.y].gauche:
                c += " gauche (q)        "
            if not self.cases[self.x][self.y].droite:
                c += " droite (d)        "
            if not self.cases[self.x][self.y].haut:
                c += " haut (z)        "
            if not self.cases[self.x][self.y].bas:
                c += " bas (s)        "
            c += " suicide (a)"
            print(c)
            c = input()
        
        if c == "a":
            self.arret = False        
            for i in range(len(self.fantomes)):
                self.fantomes[i].arret = False
            for i in range(len(self.fantomes)):
                self.fantomes[i].pasmanger = True
            self.suicide()

        self.arret = False        
        for i in range(len(self.fantomes)):
            self.fantomes[i].arret = False
        
        if c == "q":
            return Action.gauche
        if c == "d":
            return Action.droite
        if c == "z":
            return Action.monter
        if c == "s":
            return Action.descendre
       


    def attaquer(self):
        test = False
        gommeH = False
        gommeB = False
        gommeG = False
        gommeD = False
        if not self.cases[self.x][self.y].gauche:
            gommeG = True
        if not self.cases[self.x][self.y].droite:
            gommeD = True
        if not self.cases[self.x][self.y].haut:
            gommeH = True
        if not self.cases[self.x][self.y].bas:
            gommeB = True
        #choisi une action au hasard parmi celle possible puis regarde si un fantome se trouve sur la ligne ou la colonne concerné
        #   si c'est le cas, change d'action, jusqu'à ce que plus aucune soit possible
        listeActionsPossibles = [
            gommeG == True,  # mur == true => true
            gommeD == True,
            gommeH == True,
            gommeB == True
        ]
        r = random.randint(0, 3)  # aléatoire
        while not listeActionsPossibles[r]:  # si mur == true
            r = random.randint(0, 3)  # => relance aléatoire

        if r == 0: # on veut aller à gauche
            for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                if self.fantomes[i].x == self.x:
                    if self.fantomes[i].y < self.y:
                        j = self.y
                        t = False
                        while j > self.fantomes[i].y and t == False:
                            if self.cases[self.x][j].gauche:
                                t = True
                            j -= 1
                        if t:
                            return Action.gauche  
        elif r == 1:
            for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                if self.fantomes[i].x == self.x:
                    if self.fantomes[i].y > self.y:
                        j = self.y
                        t = False
                        while j < self.fantomes[i].y and t == False:
                            if self.cases[self.x][j].droite:
                                t = True
                            j += 1
                        if t:
                            return Action.droite
        elif r == 2:
            for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                if self.fantomes[i].y == self.y:
                    if self.fantomes[i].x < self.x:
                        j = self.x
                        t = False
                        while j > self.fantomes[i].x and t == False:
                            if self.cases[j][self.y].haut:
                                t = True
                            j -= 1
                        if t:
                            return Action.monter
        else :
            for i in range(len(self.fantomes)): # on regarde si un fantome est dans la direction
                if self.fantomes[i].y == self.y:
                    if self.fantomes[i].x > self.x:
                        j = self.x
                        t = False
                        while j < self.fantomes[i].x and t == False:
                            if self.cases[j][self.y].bas:
                                t = True
                            j += 1
                        if t:
                            return Action.descendre
        return self.chercher()
        
        
   

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
        if self.cases[self.x][self.y].gomme in [Gomme.gomme, Gomme.superGomme]:
            if self.cases[self.x][self.y].gomme == Gomme.superGomme:
                self.ticks = 10
                self.objectif = ObjectifPac.attaquer
            self.cases[self.x][self.y].gomme = Gomme.vide
            self.background.delete(self.cases[self.x][self.y].sprite)
            self.nb_gomme -= 1
            if self.nb_gomme == 0:
                self.statusPartie.set(Status.gagne.value)

    def tuer(self):
        if self.objectif == ObjectifPac.attaquer:
            for i in range (len(self.fantomes)):
                if self.fantomes[i].x == self.x and self.fantomes[i].y == self.y:
                    self.fantomes[i].mourir()

    def mourir(self):
        self.background.delete(self.sprite)
        self.statusPartie.set(Status.perdu.value)

    def suicide(self):
        self.background.delete(self.sprite)
        self.statusPartie.set(Status.suicide.value)