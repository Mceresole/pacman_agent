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

cases = [[]]
cases[0].append(Case(0, 0, True, False, False, True))
cases[0].append(Case(0, 1, True, False, False, False))

for y in range(2, 5):
    cases[0].append(Case(0, y, True, True, False, False))

cases[0].append(Case(0, 5, True, False, False, False))

for y in range(6, 9):
    cases[0].append(Case(0, y, True, True, False, False))

cases[0].append(Case(0, 9, True, False, True, False))
cases[0].append(Case(0, 10, True, False, False, True))

for y in range(11, 14):
    cases[0].append(Case(0, y, True, True, False, False))

cases[0].append(Case(0, 14, True, False, False, False))

for y in range(15, 17):
    cases[0].append(Case(0, y, True, True, False, False))

cases[0].append(Case(0, 17, False, True, False, True))


for x in range(1, 17):
    cases[x].append(Case(x, 0, True, False, False, False))

cases[1].append(Case(x, 0, True, False, False, False))





for x in range(1, 17):
    cases[x].append(Case(x, 17, False, True, False, False))

cases[17].append(Case(17, 0, True, False, True, False))
for y in range(1, 17):
    cases[17].append(Case(17, y, False, False, True, False))

cases[17].append(Case(17, 17, False, True, True, False))

window.mainloop()
