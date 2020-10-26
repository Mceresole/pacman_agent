#! python3

import tkinter
import Partie
import Constants
from Enumerations import Status

window = tkinter.Tk()

FPS = tkinter.IntVar()
FPS.set(1)

window.title("Pac Man")
window.geometry(str(Constants.t) + "x" + str(Constants.h))
window.resizable(width=False, height=False)

background = tkinter.Canvas(window, width=Constants.t, height=Constants.t, background="#000", bd=0, highlightthickness=0)
background.pack()

controls = tkinter.Toplevel()

controls.resizable(width = False, height = False)
controls.title("Contrôles")
controls.geometry("200x350")

statusPartie = tkinter.StringVar()
statusPartie.set(Status.pause.value)

Partie.initialize()

labelPartie = tkinter.Label(controls, textvariable=statusPartie)
buttonPartie = tkinter.Button(controls, command=Partie.start)
labelVitesse = tkinter.Label(controls, text="Vitesse:") # modifier vitesse
scaleVitesse = tkinter.Scale(controls, orient=tkinter.HORIZONTAL, from_=1, to=60, length=180, variable=FPS, cursor='sb_h_double_arrow') # Curseur pour modifier les FPS

labelPartie.pack()
buttonPartie.pack()
labelVitesse.pack()
scaleVitesse.pack()

window.mainloop()
