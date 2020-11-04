import tkinter
import Constants
from Enumerations import Status
from Partie import Partie


"""
Object statique représentant l'application graphique.
"""
class App():

    def __init__(self):
        self.window = tkinter.Tk()
        self.FPS = tkinter.IntVar()
        self.background = tkinter.Canvas(self.window, width=Constants.t, height=Constants.t, background="#000", bd=0, highlightthickness=0)
        self.controls = tkinter.Toplevel()
        self.statusPartie = tkinter.StringVar()
        self.labelPartie = tkinter.Label(self.controls, textvariable=self.statusPartie)
        self.buttonPartie = tkinter.Button(self.controls, command=Partie.Partie.start)
        self.labelVitesse = tkinter.Label(self.controls, text="Vitesse:")  # modifier vitesse
        self.scaleVitesse = tkinter.Scale(self.controls, orient=tkinter.HORIZONTAL, from_=1, to=60, length=180, variable=self.FPS, cursor='sb_h_double_arrow')  # Curseur pour modifier les FPS
        self.FPS.set(1)
        self.window.title("Pac Man")
        self.window.geometry(str(Constants.t) + "x" + str(Constants.h))
        self.window.resizable(width=False, height=False)
        self.background.pack()
        self.controls.resizable(width = False, height = False)
        self.controls.title("Contrôles")
        self.controls.geometry("200x350")
        self.statusPartie.set(Status.pause.value)
        self.partie = Partie()
        self.partie.initialize()
        self.labelPartie.pack()
        self.buttonPartie.pack()
        self.labelVitesse.pack()
        self.scaleVitesse.pack()
        self.window.mainloop()