import tkinter

window = tkinter.Tk()

t = 1000
l = 1000 / 18
e = 10

window.title("Pac Man")
window.geometry(str(t)+"x"+str(t))

background = tkinter.Canvas(window, width=t, height=t, background="#000", bd=0, highlightthickness=0)
background.pack()

class Mur:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        background.create_rectangle(x1, y1, x2, y2, fill="#fff", outline="#fff")

class Case:
    # constructeur
    def __init__(self, x: int, y: int, haut: bool, bas: bool, droite: bool, gauche: bool):
        self.x = x # coordonnées case
        self.y = y
        self.haut = haut # murs en haut?
        self.bas = bas
        self.gauche = gauche
        self.droite = droite
        if haut:
            Mur(x*l, y*l, (x+1)*l, y*l+e)
        if bas:
            Mur(x*l, (y+1)*l-e, (x+1)*l, (y+1)*l)
        if gauche:
            Mur(x*l, y*l, x*l+e, (y+1)*l)
        if droite:
            Mur((x+1)*l-e, y*l, (x+1)*l, (y+1)*l)

cases = []

for x in range(0, 18):
    cases.append([])

cases[0].append(Case(0, 0, True, False, False, True))

for x in range(1, 4):
    cases[x].append(Case(x, 0, True, True, False, False))

cases[4].append(Case(4, 0, True, False, False, False))

for x in range(5, 8):
    cases[x].append(Case(x, 0, True, True, False, False))

cases[8].append(Case(8, 0, True, False, True, False))
cases[9].append(Case(9, 0, True, False, False, True))

for x in range(10, 13):
    cases[x].append(Case(x, 0, True, True, False, False))

cases[13].append(Case(13, 0, True, False, False, False))

for x in range(14, 17):
    cases[x].append(Case(x, 0, True, True, False, False))

cases[17].append(Case(17, 0, True, False, True, False))

for y in range(1, 17):
    cases[0].append(Case(0, y, False, False, False, True))

cases[0].append(Case(0, 17, False, True, False, True))



for x in range(1, 17):
    cases[x].append(Case(x, 17, False, True, False, False))

cases[17].append(Case(17, 0, True, False, True, False))
for y in range(1, 17):
    cases[17].append(Case(17, y, False, False, True, False))

cases[17].append(Case(17, 17, False, True, True, False))

window.mainloop()
