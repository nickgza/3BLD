from enums import Colour, Face, Move

class Piece:
    colours: tuple[Colour]
    orientation: Face

    __match_args__ = ('colours',)

    def __init__(self, colours: tuple[Colour], orientation: Face):
        self.colours = colours
        self.orientation = orientation

    def __str__(self):
        return f'{self.colours}  {self.orientation}'

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: 'Piece'):
        return self.colours == other.colours
    
    def __hash__(self):
        return hash(self.colours)

    def change_orientation(self, move: Move | str):
        match move:
            case Move.U | Move.Dp | Move.Ep | "U" | "D'" | "E'":
                match self.orientation:
                    case Face.F: self.orientation = Face.L
                    case Face.L: self.orientation = Face.B
                    case Face.B: self.orientation = Face.R
                    case Face.R: self.orientation = Face.F
            case Move.Up | Move.D | Move.E | "U'" | "D" | "E":
                match self.orientation:
                    case Face.F: self.orientation = Face.R
                    case Face.L: self.orientation = Face.F
                    case Face.B: self.orientation = Face.L
                    case Face.R: self.orientation = Face.B
            case Move.U2 | Move.D2 | Move.E2 | "U2" | "D2" | "E2":
                match self.orientation:
                    case Face.F: self.orientation = Face.B
                    case Face.L: self.orientation = Face.R
                    case Face.B: self.orientation = Face.F
                    case Face.R: self.orientation = Face.L
            case Move.L | Move.Rp | Move.M | "L" | "R'" | "M":
                match self.orientation:
                    case Face.U: self.orientation = Face.F
                    case Face.F: self.orientation = Face.D
                    case Face.D: self.orientation = Face.B
                    case Face.B: self.orientation = Face.U
            case Move.Lp | Move.R | Move.Mp | "L'" | "R" | "M'":
                match self.orientation:
                    case Face.U: self.orientation = Face.B
                    case Face.F: self.orientation = Face.U
                    case Face.D: self.orientation = Face.F
                    case Face.B: self.orientation = Face.D
            case Move.L2 | Move.R2 | Move.M2 | "L2" | "R2" | "M2":
                match self.orientation:
                    case Face.U: self.orientation = Face.D
                    case Face.F: self.orientation = Face.B
                    case Face.D: self.orientation = Face.U
                    case Face.B: self.orientation = Face.F
            case Move.F | Move.Bp | Move.S | "F" | "B'" | "S":
                match self.orientation:
                    case Face.U: self.orientation = Face.R
                    case Face.R: self.orientation = Face.D
                    case Face.D: self.orientation = Face.L
                    case Face.L: self.orientation = Face.U
            case Move.Fp | Move.B | Move.Sp | "F'" | "B" | "S'":
                match self.orientation:
                    case Face.U: self.orientation = Face.L
                    case Face.R: self.orientation = Face.U
                    case Face.D: self.orientation = Face.R
                    case Face.L: self.orientation = Face.D
            case Move.F2 | Move.B2 | Move.S2 | "F2" | "B2" | "S2":
                match self.orientation:
                    case Face.U: self.orientation = Face.D
                    case Face.R: self.orientation = Face.L
                    case Face.D: self.orientation = Face.U
                    case Face.L: self.orientation = Face.R

class Corner(Piece):
    def __init__(self, colours: tuple[Colour], orientation: Face = None):
        assert len(colours) == 3
        super().__init__(colours, orientation)

class Edge(Piece):
    def __init__(self, colours: tuple[Colour], orientation: Face = None):
        assert len(colours) == 2
        super().__init__(colours, orientation)
