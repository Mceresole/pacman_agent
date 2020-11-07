from enum import Enum

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
    sortir = 3

class Status(Enum):
    pause = "Partie en pause"
    enCours = "Partie en cours"
    perdu = "Perdu !"
    gagne = "Gagné !"