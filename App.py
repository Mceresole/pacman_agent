import tkinter
import Constants
from Enumerations import Status
from Partie import Partie


"""
Object statique représentant l'application graphique.
"""
class App(object):
    window = tkinter.Tk()
    FPS = tkinter.IntVar()
    background = tkinter.Canvas(window, width=Constants.t, height=Constants.t, background="#000", bd=0, highlightthickness=0)
    controls = tkinter.Toplevel()
    statusPartie = tkinter.StringVar()
    labelPartie = tkinter.Label(controls, textvariable=statusPartie)
    buttonPartie = tkinter.Button(controls, command=Partie.Partie.start)
    labelVitesse = tkinter.Label(controls, text="Vitesse:")  # modifier vitesse
    scaleVitesse = tkinter.Scale(controls, orient=tkinter.HORIZONTAL, from_=1, to=60, length=180, variable=FPS, cursor='sb_h_double_arrow')  # Curseur pour modifier les FPS

    @staticmethod
    def initialize():
        App.FPS.set(1)
        App.window.title("Pac Man")
        App.window.geometry(str(Constants.t) + "x" + str(Constants.h))
        App.window.resizable(width=False, height=False)
        App.background.pack()
        App.controls.resizable(width = False, height = False)
        App.controls.title("Contrôles")
        App.controls.geometry("200x350")
        App.statusPartie.set(Status.pause.value)
        Partie.initialize()
        App.labelPartie.pack()
        App.buttonPartie.pack()
        App.labelVitesse.pack()
        App.scaleVitesse.pack()
        App.window.mainloop()