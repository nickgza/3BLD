from enums import Colour, Face, Move

class Piece:
    colours: tuple[Colour]
    orientation: Face
    orientation2: Face

    __match_args__ = ('colours',)

    def __init__(self, colours: tuple[Colour], orientation: Face, orientation2: Face):
        self.colours = colours
        self.orientation = orientation
        self.orientation2 = orientation2

    def __str__(self):
        return f'{self.colours}  {self.orientation}/{self.orientation2}'

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: 'Piece'):
        return self.colours == other.colours
    
    def __hash__(self):
        return hash(self.colours)

    def change_orientation(self, move: Move | str):
        for orientation in ['orientation', 'orientation2']:
            match move:
                case Move.U | Move.Dp | Move.Ep | "U" | "D'" | "E'":
                    match getattr(self, orientation):
                        case Face.F: setattr(self, orientation, Face.L)
                        case Face.L: setattr(self, orientation, Face.B)
                        case Face.B: setattr(self, orientation, Face.R)
                        case Face.R: setattr(self, orientation, Face.F)
                case Move.Up | Move.D | Move.E | "U'" | "D" | "E":
                    match getattr(self, orientation):
                        case Face.F: setattr(self, orientation, Face.R)
                        case Face.L: setattr(self, orientation, Face.F)
                        case Face.B: setattr(self, orientation, Face.L)
                        case Face.R: setattr(self, orientation, Face.B)
                case Move.U2 | Move.D2 | Move.E2 | "U2" | "D2" | "E2":
                    match getattr(self, orientation):
                        case Face.F: setattr(self, orientation, Face.B)
                        case Face.L: setattr(self, orientation, Face.R)
                        case Face.B: setattr(self, orientation, Face.F)
                        case Face.R: setattr(self, orientation, Face.L)
                case Move.L | Move.Rp | Move.M | "L" | "R'" | "M":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.F)
                        case Face.F: setattr(self, orientation, Face.D)
                        case Face.D: setattr(self, orientation, Face.B)
                        case Face.B: setattr(self, orientation, Face.U)
                case Move.Lp | Move.R | Move.Mp | "L'" | "R" | "M'":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.B)
                        case Face.F: setattr(self, orientation, Face.U)
                        case Face.D: setattr(self, orientation, Face.F)
                        case Face.B: setattr(self, orientation, Face.D)
                case Move.L2 | Move.R2 | Move.M2 | "L2" | "R2" | "M2":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.D)
                        case Face.F: setattr(self, orientation, Face.B)
                        case Face.D: setattr(self, orientation, Face.U)
                        case Face.B: setattr(self, orientation, Face.F)
                case Move.F | Move.Bp | Move.S | "F" | "B'" | "S":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.R)
                        case Face.R: setattr(self, orientation, Face.D)
                        case Face.D: setattr(self, orientation, Face.L)
                        case Face.L: setattr(self, orientation, Face.U)
                case Move.Fp | Move.B | Move.Sp | "F'" | "B" | "S'":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.L)
                        case Face.R: setattr(self, orientation, Face.U)
                        case Face.D: setattr(self, orientation, Face.R)
                        case Face.L: setattr(self, orientation, Face.D)
                case Move.F2 | Move.B2 | Move.S2 | "F2" | "B2" | "S2":
                    match getattr(self, orientation):
                        case Face.U: setattr(self, orientation, Face.D)
                        case Face.R: setattr(self, orientation, Face.L)
                        case Face.D: setattr(self, orientation, Face.U)
                        case Face.L: setattr(self, orientation, Face.R)

class Corner(Piece):
    def __init__(self, colours: tuple[Colour], orientation: Face = None, orientation2: Face = None):
        assert len(colours) == 3
        super().__init__(colours, orientation, orientation2)

class Edge(Piece):
    def __init__(self, colours: tuple[Colour], orientation: Face = None, orientation2: Face = None):
        assert len(colours) == 2
        super().__init__(colours, orientation, orientation2)
