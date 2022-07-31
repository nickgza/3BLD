from enums import Colour as C, Face as F, Move
from piece import Corner, Edge
import numpy as np

class Cube:
    pieces: np.ndarray

    def __init__(self):
        self.pieces = np.array([
            [[Corner([C.WHITE, C.GREEN, C.ORANGE], F.U) , Edge([C.WHITE, C.GREEN], F.U) , Corner([C.WHITE, C.RED, C.GREEN], F.U)],
             [Edge([C.GREEN, C.ORANGE], F.F)            , None                          , Edge([C.GREEN, C.RED], F.F)],
             [Corner([C.YELLOW, C.ORANGE, C.GREEN], F.D), Edge([C.YELLOW, C.GREEN], F.D), Corner([C.YELLOW, C.GREEN, C.RED], F.D)]],
            [[Edge([C.WHITE, C.ORANGE], F.U)            , None                          , Edge([C.WHITE, C.RED], F.U)],
             [None                                      , None                          , None],
             [Edge([C.YELLOW, C.ORANGE], F.D)           , None                          , Edge([C.YELLOW, C.RED], F.D)]],
            [[Corner([C.WHITE, C.ORANGE, C.BLUE], F.U)  , Edge([C.WHITE, C.BLUE], F.U)  , Corner([C.WHITE, C.BLUE, C.RED], F.U)],
             [Edge([C.BLUE, C.ORANGE], F.B)             , None                          , Edge([C.BLUE, C.RED], F.B)],
             [Corner([C.YELLOW, C.BLUE, C.ORANGE], F.D) , Edge([C.YELLOW, C.BLUE], F.D) , Corner([C.YELLOW, C.RED, C.BLUE], F.D)]]
        ])
    
    def __str__(self):
        return str(self.pieces)
    
    def get_letter(self, tup: tuple[Corner | Edge, int]) -> str:
        piece, orientation = tup
        if isinstance(piece, Corner):
            match piece:
                case Corner([C.WHITE, C.ORANGE, C.BLUE]):
                    return 'A' if orientation == 0 else 'E' if orientation == 1 else 'R'
                case Corner([C.WHITE, C.BLUE, C.RED]):
                    return 'B' if orientation == 0 else 'Q' if orientation == 1 else 'N'
                case Corner([C.WHITE, C.RED, C.GREEN]):
                    return 'C' if orientation == 0 else 'M' if orientation == 1 else 'J'
                case Corner([C.WHITE, C.GREEN, C.ORANGE]):
                    return 'D' if orientation == 0 else 'I' if orientation == 1 else 'F'
                case Corner([C.YELLOW, C.ORANGE, C.GREEN]):
                    return 'U' if orientation == 0 else 'G' if orientation == 1 else 'L'
                case Corner([C.YELLOW, C.GREEN, C.RED]):
                    return 'V' if orientation == 0 else 'K' if orientation == 1 else 'P'
                case Corner([C.YELLOW, C.RED, C.BLUE]):
                    return 'W' if orientation == 0 else 'O' if orientation == 1 else 'T'
                case Corner([C.YELLOW, C.BLUE, C.ORANGE]):
                    return 'X' if orientation == 0 else 'S' if orientation == 1 else 'H'
        elif isinstance(piece, Edge):
            match piece:
                case Edge([C.WHITE, C.BLUE]):
                    return 'A' if orientation == 0 else 'Q'
                case Edge([C.WHITE, C.RED]):
                    return 'B' if orientation == 0 else 'M'
                case Edge([C.WHITE, C.GREEN]):
                    return 'C' if orientation == 0 else 'I'
                case Edge([C.WHITE, C.ORANGE]):
                    return 'D' if orientation == 0 else 'E'
                case Edge([C.GREEN, C.ORANGE]):
                    return 'L' if orientation == 0 else 'F'
                case Edge([C.GREEN, C.RED]):
                    return 'J' if orientation == 0 else 'P'
                case Edge([C.BLUE, C.RED]):
                    return 'T' if orientation == 0 else 'N'
                case Edge([C.BLUE, C.ORANGE]):
                    return 'R' if orientation == 0 else 'H'
                case Edge([C.YELLOW, C.GREEN]):
                    return 'U' if orientation == 0 else 'K'
                case Edge([C.YELLOW, C.RED]):
                    return 'V' if orientation == 0 else 'O'
                case Edge([C.YELLOW, C.BLUE]):
                    return 'W' if orientation == 0 else 'S'
                case Edge([C.YELLOW, C.ORANGE]):
                    return 'X' if orientation == 0 else 'G'
    
    def make_moves(self, moves: str):
        for move in moves.split():
            self.make_move(move)
    
    def make_move(self, move: Move | str):
        match move:
            case Move.U | "U":
                for piece in np.nditer(self.pieces[:, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 0] = np.rot90(self.pieces[:, 0])
            case Move.Up | "U'":
                for piece in np.nditer(self.pieces[:, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 0] = np.rot90(self.pieces[:, 0], -1)
            case Move.U2 | "U2":
                for piece in np.nditer(self.pieces[:, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 0] = np.rot90(self.pieces[:, 0], 2)
            case Move.D | "D":
                for piece in np.nditer(self.pieces[:, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 2] = np.rot90(self.pieces[:, 2], -1)
            case Move.Dp | "D'":
                for piece in np.nditer(self.pieces[:, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 2] = np.rot90(self.pieces[:, 2])
            case Move.D2 | "D2":
                for piece in np.nditer(self.pieces[:, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 2] = np.rot90(self.pieces[:, 2], 2)
            case Move.E | "E":
                for piece in np.nditer(self.pieces[:, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 1] = np.rot90(self.pieces[:, 1], -1)
            case Move.Ep | "E'":
                for piece in np.nditer(self.pieces[:, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 1] = np.rot90(self.pieces[:, 1])
            case Move.E2 | "E2":
                for piece in np.nditer(self.pieces[:, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, 1] = np.rot90(self.pieces[:, 1], 2)
            case Move.L | "L":
                for piece in np.nditer(self.pieces[:, :, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 0] = np.rot90(self.pieces[:, :, 0], -1)
            case Move.Lp | "L'":
                for piece in np.nditer(self.pieces[:, :, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 0] = np.rot90(self.pieces[:, :, 0])
            case Move.L2 | "L2":
                for piece in np.nditer(self.pieces[:, :, 0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 0] = np.rot90(self.pieces[:, :, 0], 2)
            case Move.R | "R":
                for piece in np.nditer(self.pieces[:, :, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 2] = np.rot90(self.pieces[:, :, 2])
            case Move.Rp | "R'":
                for piece in np.nditer(self.pieces[:, :, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 2] = np.rot90(self.pieces[:, :, 2], -1)
            case Move.R2 | "R2":
                for piece in np.nditer(self.pieces[:, :, 2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 2] = np.rot90(self.pieces[:, :, 2], 2)
            case Move.M | "M":
                for piece in np.nditer(self.pieces[:, :, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 1] = np.rot90(self.pieces[:, :, 1], -1)
            case Move.Mp | "M'":
                for piece in np.nditer(self.pieces[:, :, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 1] = np.rot90(self.pieces[:, :, 1])
            case Move.M2 | "M2":
                for piece in np.nditer(self.pieces[:, :, 1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[:, :, 1] = np.rot90(self.pieces[:, :, 1], 2)
            case Move.F | "F":
                for piece in np.nditer(self.pieces[0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[0] = np.rot90(self.pieces[0], -1)
            case Move.Fp | "F'":
                for piece in np.nditer(self.pieces[0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[0] = np.rot90(self.pieces[0])
            case Move.F2 | "F2":
                for piece in np.nditer(self.pieces[0], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[0] = np.rot90(self.pieces[0], 2)
            case Move.B | "B":
                for piece in np.nditer(self.pieces[2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[2] = np.rot90(self.pieces[2])
            case Move.Bp | "B'":
                for piece in np.nditer(self.pieces[2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[2] = np.rot90(self.pieces[2], -1)
            case Move.B2 | "B2":
                for piece in np.nditer(self.pieces[2], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[2] = np.rot90(self.pieces[2], 2)
            case Move.S | "S":
                for piece in np.nditer(self.pieces[1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[1] = np.rot90(self.pieces[1], -1)
            case Move.Sp | "S'":
                for piece in np.nditer(self.pieces[1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[1] = np.rot90(self.pieces[1])
            case Move.S2 | "S2":
                for piece in np.nditer(self.pieces[1], flags=['refs_ok']):
                    piece = piece.item()
                    if piece is not None: piece.change_orientation(move)
                self.pieces[1] = np.rot90(self.pieces[1], 2)
    
    def get_edge(self, letter: str) -> tuple[Edge, int]:
        match letter:
            case 'A':
                piece = self.pieces[2, 0, 1]
                return (piece, 0 if piece.orientation == F.U else 1)
            case 'Q':
                piece = self.pieces[2, 0, 1]
                return (piece, 0 if piece.orientation == F.B else 1)
            case 'B':
                piece = self.pieces[1, 0, 2]
                return (piece, 0 if piece.orientation == F.U else 1)
            case 'M':
                piece = self.pieces[1, 0, 2]
                return (piece, 0 if piece.orientation == F.R else 1)
            case 'C':
                piece = self.pieces[0, 0, 1]
                return (piece, 0 if piece.orientation == F.U else 1)
            case 'I':
                piece = self.pieces[0, 0, 1]
                return (piece, 0 if piece.orientation == F.F else 1)
            case 'D':
                piece = self.pieces[1, 0, 0]
                return (piece, 0 if piece.orientation == F.U else 1)
            case 'E':
                piece = self.pieces[1, 0, 0]
                return (piece, 0 if piece.orientation == F.L else 1)
            case 'L':
                piece = self.pieces[0, 1, 0]
                return (piece, 0 if piece.orientation == F.F else 1)
            case 'F':
                piece = self.pieces[0, 1, 0]
                return (piece, 0 if piece.orientation == F.L else 1)
            case 'J':
                piece = self.pieces[0, 1, 2]
                return (piece, 0 if piece.orientation == F.F else 1)
            case 'P':
                piece = self.pieces[0, 1, 2]
                return (piece, 0 if piece.orientation == F.R else 1)
            case 'T':
                piece = self.pieces[2, 1, 2]
                return (piece, 0 if piece.orientation == F.B else 1)
            case 'N':
                piece = self.pieces[2, 1, 2]
                return (piece, 0 if piece.orientation == F.R else 1)
            case 'R':
                piece = self.pieces[2, 1, 0]
                return (piece, 0 if piece.orientation == F.B else 1)
            case 'H':
                piece = self.pieces[2, 1, 0]
                return (piece, 0 if piece.orientation == F.L else 1)
            case 'U':
                piece = self.pieces[0, 2, 1]
                return (piece, 0 if piece.orientation == F.D else 1)
            case 'K':
                piece = self.pieces[0, 2, 1]
                return (piece, 0 if piece.orientation == F.F else 1)
            case 'V':
                piece = self.pieces[1, 2, 2]
                return (piece, 0 if piece.orientation == F.D else 1)
            case 'O':
                piece = self.pieces[1, 2, 2]
                return (piece, 0 if piece.orientation == F.R else 1)
            case 'W':
                piece = self.pieces[2, 2, 1]
                return (piece, 0 if piece.orientation == F.D else 1)
            case 'S':
                piece = self.pieces[2, 2, 1]
                return (piece, 0 if piece.orientation == F.B else 1)
            case 'X':
                piece = self.pieces[1, 2, 0]
                return (piece, 0 if piece.orientation == F.D else 1)
            case 'G':
                piece = self.pieces[1, 2, 0]
                return (piece, 0 if piece.orientation == F.L else 1)
                
    def get_corner(self, letter: str) -> tuple[Corner, int]:
        match letter:
            case 'A':
                piece = self.pieces[2, 0, 0]
                return (piece, 0 if piece.orientation == F.U else 1 if piece.orientation == F.B else 2)
            case 'E':
                piece = self.pieces[2, 0, 0]
                return (piece, 0 if piece.orientation == F.L else 1 if piece.orientation == F.U else 2)
            case 'R':
                piece = self.pieces[2, 0, 0]
                return (piece, 0 if piece.orientation == F.B else 1 if piece.orientation == F.L else 2)
            case 'B':
                piece = self.pieces[2, 0, 2]
                return (piece, 0 if piece.orientation == F.U else 1 if piece.orientation == F.R else 2)
            case 'Q':
                piece = self.pieces[2, 0, 2]
                return (piece, 0 if piece.orientation == F.B else 1 if piece.orientation == F.U else 2)
            case 'N':
                piece = self.pieces[2, 0, 2]
                return (piece, 0 if piece.orientation == F.R else 1 if piece.orientation == F.B else 2)
            case 'C':
                piece = self.pieces[0, 0, 2]
                return (piece, 0 if piece.orientation == F.U else 1 if piece.orientation == F.F else 2)
            case 'M':
                piece = self.pieces[0, 0, 2]
                return (piece, 0 if piece.orientation == F.R else 1 if piece.orientation == F.U else 2)
            case 'J':
                piece = self.pieces[0, 0, 2]
                return (piece, 0 if piece.orientation == F.F else 1 if piece.orientation == F.R else 2)
            case 'D':
                piece = self.pieces[0, 0, 0]
                return (piece, 0 if piece.orientation == F.U else 1 if piece.orientation == F.L else 2)
            case 'I':
                piece = self.pieces[0, 0, 0]
                return (piece, 0 if piece.orientation == F.F else 1 if piece.orientation == F.U else 2)
            case 'F':
                piece = self.pieces[0, 0, 0]
                return (piece, 0 if piece.orientation == F.L else 1 if piece.orientation == F.F else 2)
            case 'U':
                piece = self.pieces[0, 2, 0]
                return (piece, 0 if piece.orientation == F.D else 1 if piece.orientation == F.F else 2)
            case 'G':
                piece = self.pieces[0, 2, 0]
                return (piece, 0 if piece.orientation == F.L else 1 if piece.orientation == F.D else 2)
            case 'L':
                piece = self.pieces[0, 2, 0]
                return (piece, 0 if piece.orientation == F.F else 1 if piece.orientation == F.L else 2)
            case 'V':
                piece = self.pieces[0, 2, 2]
                return (piece, 0 if piece.orientation == F.D else 1 if piece.orientation == F.R else 2)
            case 'K':
                piece = self.pieces[0, 2, 2]
                return (piece, 0 if piece.orientation == F.F else 1 if piece.orientation == F.D else 2)
            case 'P':
                piece = self.pieces[0, 2, 2]
                return (piece, 0 if piece.orientation == F.R else 1 if piece.orientation == F.F else 2)
            case 'W':
                piece = self.pieces[2, 2, 2]
                return (piece, 0 if piece.orientation == F.D else 1 if piece.orientation == F.B else 2)
            case 'O':
                piece = self.pieces[2, 2, 2]
                return (piece, 0 if piece.orientation == F.R else 1 if piece.orientation == F.D else 2)
            case 'T':
                piece = self.pieces[2, 2, 2]
                return (piece, 0 if piece.orientation == F.B else 1 if piece.orientation == F.R else 2)
            case 'X':
                piece = self.pieces[2, 2, 0]
                return (piece, 0 if piece.orientation == F.D else 1 if piece.orientation == F.L else 2)
            case 'S':
                piece = self.pieces[2, 2, 0]
                return (piece, 0 if piece.orientation == F.B else 1 if piece.orientation == F.D else 2)
            case 'H':
                piece = self.pieces[2, 2, 0]
                return (piece, 0 if piece.orientation == F.L else 1 if piece.orientation == F.B else 2)
