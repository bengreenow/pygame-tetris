from enum import Enum

class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.gridArray = []

        for row in range(h):
            temp = []
            for col in range(w):
                temp.append(0)
            self.gridArray.append(temp)

class Shape(Enum):
    S = 0
    Z = 1
    T = 2
    L = 3
    LINE = 4
    MIRRORED_L = 5
    SQUARE = 6

class Tetrimino:
    def __init__():

g = Grid(10,30)
