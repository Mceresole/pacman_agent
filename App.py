import tkinter
from Constants import t, h
from Enumerations import Status
from Partie import Partie


class App:

    def __init__(self):
        self.window = tkinter.Tk()
        self.background = tkinter.Canvas(self.window, width=t, height=t, background="#000", bd=0, highlightthickness=0)
        self.controls = tkinter.Toplevel()
        self.statusPartie = tkinter.StringVar()
        self.partie = Partie(self.window, self.background, self.statusPartie, self.controls)
        self.window.bind("<Button-1>", self.partie.start)
        self.window.title("Pac Man")
        self.window.geometry(str(t) + "x" + str(h))
        self.window.resizable(width=False, height=False)
        self.background.pack()
        self.statusPartie.set(Status.pause.value)
        self.window.mainloop()