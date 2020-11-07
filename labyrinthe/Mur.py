class Mur:
    def __init__(self, x1, y1, x2, y2, background):
        self.background = background
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.background.create_rectangle(x1, y1, x2, y2, fill="#fff", outline="#fff")