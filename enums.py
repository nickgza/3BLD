from enum import Enum

class Colour(Enum):
    WHITE = 1
    YELLOW = 2
    ORANGE = 3
    RED = 4
    GREEN = 5
    BLUE = 6

    def __repr__(self):
        return self.name

class Face(Enum):
    U = 1
    D = 2
    L = 3
    R = 4
    F = 5
    B = 6

class Move(Enum):
    U = "U"
    Up = "U'"
    U2 = "U2"
    D = "D"
    Dp = "D'"
    D2 = "D2"
    L = "L"
    Lp = "L'"
    L2 = "L2"
    R = "R"
    Rp = "R'"
    R2 = "R2"
    F = "F"
    Fp = "F'"
    F2 = "F2"
    B = "B"
    Bp = "B'"
    B2 = "B2"
    M = "M"
    Mp = "M'"
    M2 = "M2"
    E = "E"
    Ep = "E'"
    E2 = "E2"
    S = "S"
    Sp = "S'"
    S2 = "S2"
