from enums import Colour as C, Face as F, Move
from piece import Corner, Edge
import numpy as np
import random

class Cube:
    pieces: np.ndarray

    POCHMANN_CORNERS_ALGORITHM: str = "R U' R' U' R U R' F' R U R' U' R' F R"
    M2_EDGES_ALGORITHM: str = "M2"

    SOLVED_CUBE = np.array([
        [[Corner((C.WHITE, C.GREEN, C.ORANGE), F.U, F.F) , Edge((C.WHITE, C.GREEN), F.U, F.F) , Corner((C.WHITE, C.RED, C.GREEN), F.U, F.R)],
         [Edge((C.GREEN, C.ORANGE), F.F, F.L)            , None                               , Edge((C.GREEN, C.RED), F.F, F.R)],
         [Corner((C.YELLOW, C.ORANGE, C.GREEN), F.D, F.L), Edge((C.YELLOW, C.GREEN), F.D, F.F), Corner((C.YELLOW, C.GREEN, C.RED), F.D, F.F)]],
        [[Edge((C.WHITE, C.ORANGE), F.U, F.L)            , None                               , Edge((C.WHITE, C.RED), F.U, F.R)],
         [None                                           , None                               , None],
         [Edge((C.YELLOW, C.ORANGE), F.D, F.L)           , None                               , Edge((C.YELLOW, C.RED), F.D, F.R)]],
        [[Corner((C.WHITE, C.ORANGE, C.BLUE), F.U, F.L)  , Edge((C.WHITE, C.BLUE), F.U, F.B)  , Corner((C.WHITE, C.BLUE, C.RED), F.U, F.B)],
         [Edge((C.BLUE, C.ORANGE), F.B, F.L)             , None                               , Edge((C.BLUE, C.RED), F.B, F.R)],
         [Corner((C.YELLOW, C.BLUE, C.ORANGE), F.D, F.B) , Edge((C.YELLOW, C.BLUE), F.D, F.B) , Corner((C.YELLOW, C.RED, C.BLUE), F.D, F.R)]]
    ])

    def __init__(self):
        self.pieces = self.SOLVED_CUBE
    
    def generate_scramble(self, length=15) -> str:
        moves = ["U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"]
        scramble = []

        while len(scramble) < length:
            move = random.choice(moves)
            if scramble and scramble[-1][0] == move[0]:
                continue
            if len(scramble) >= 2 and scramble[-2][0] == move[0] and scramble[-1][0] == {
                'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L', 'F': 'B', 'B': 'F'
            }[move[0]]:
                continue
            scramble.append(move)

        return ' '.join(scramble)

    def pochmann_corners(self, new_cycle_order: str = 'VJBUWXI') -> str:
        '''Returns the sequence of letters for corners. New cycles are searched for in order of new_cycle_order'''
        letters: list[str] = []

        unsolved = {Corner((C.WHITE, C.GREEN, C.ORANGE)),
                    Corner((C.WHITE, C.RED, C.GREEN)),
                    Corner((C.YELLOW, C.ORANGE, C.GREEN)),
                    Corner((C.YELLOW, C.GREEN, C.RED)),
                    Corner((C.WHITE, C.ORANGE, C.BLUE)),
                    Corner((C.WHITE, C.BLUE, C.RED)),
                    Corner((C.YELLOW, C.BLUE, C.ORANGE)),
                    Corner((C.YELLOW, C.RED, C.BLUE))}
        
        current_piece, current_orientation = self.get_corner('E')
        start_piece = current_piece

        while True:
            next_letter = self.get_letter(current_piece, current_orientation)
            next_piece, next_orientation = self.get_corner(next_letter)

            if next_piece != start_piece:
                letters.append(next_letter)
                unsolved.remove(next_piece)
                current_piece, current_orientation = next_piece, next_orientation
            else:
                if current_piece != Corner((C.WHITE, C.ORANGE, C.BLUE)): # buffer piece
                    letters.append(next_letter)
                unsolved.remove(start_piece)

                # find new cycle
                for letter in new_cycle_order:
                    piece, orientation = self.get_corner(letter)
                    
                    # check if piece was solved by previous cycle
                    if piece not in unsolved:
                        continue
                    
                    # check if piece is already correct
                    match letter:
                        case 'A':
                            if piece == Corner((C.WHITE, C.ORANGE, C.BLUE)) and orientation == 0: continue
                        case 'E':
                            if piece == Corner((C.WHITE, C.ORANGE, C.BLUE)) and orientation == 1: continue
                        case 'R':
                            if piece == Corner((C.WHITE, C.ORANGE, C.BLUE)) and orientation == 2: continue
                        case 'B':
                            if piece == Corner((C.WHITE, C.BLUE, C. RED)) and orientation == 0: continue
                        case 'Q':
                            if piece == Corner((C.WHITE, C.BLUE, C. RED)) and orientation == 1: continue
                        case 'N':
                            if piece == Corner((C.WHITE, C.BLUE, C. RED)) and orientation == 2: continue
                        case 'C':
                            if piece == Corner((C.WHITE, C.RED, C.GREEN)) and orientation == 0: continue
                        case 'M':
                            if piece == Corner((C.WHITE, C.RED, C.GREEN)) and orientation == 1: continue
                        case 'J':
                            if piece == Corner((C.WHITE, C.RED, C.GREEN)) and orientation == 2: continue
                        case 'D':
                            if piece == Corner((C.WHITE, C.GREEN, C.ORANGE)) and orientation == 0: continue
                        case 'I':
                            if piece == Corner((C.WHITE, C.GREEN, C.ORANGE)) and orientation == 1: continue
                        case 'F':
                            if piece == Corner((C.WHITE, C.GREEN, C.ORANGE)) and orientation == 2: continue
                        case 'U':
                            if piece == Corner((C.YELLOW, C.ORANGE, C.GREEN)) and orientation == 0: continue
                        case 'G':
                            if piece == Corner((C.YELLOW, C.ORANGE, C.GREEN)) and orientation == 1: continue
                        case 'L':
                            if piece == Corner((C.YELLOW, C.ORANGE, C.GREEN)) and orientation == 2: continue
                        case 'V':
                            if piece == Corner((C.YELLOW, C.GREEN, C.RED)) and orientation == 0: continue
                        case 'K':
                            if piece == Corner((C.YELLOW, C.GREEN, C.RED)) and orientation == 1: continue
                        case 'P':
                            if piece == Corner((C.YELLOW, C.GREEN, C.RED)) and orientation == 2: continue
                        case 'W':
                            if piece == Corner((C.YELLOW, C.RED, C.BLUE)) and orientation == 0: continue
                        case 'O':
                            if piece == Corner((C.YELLOW, C.RED, C.BLUE)) and orientation == 1: continue
                        case 'T':
                            if piece == Corner((C.YELLOW, C.RED, C.BLUE)) and orientation == 2: continue
                        case 'X':
                            if piece == Corner((C.YELLOW, C.BLUE, C.ORANGE)) and orientation == 0: continue
                        case 'S':
                            if piece == Corner((C.YELLOW, C.BLUE, C.ORANGE)) and orientation == 1: continue
                        case 'H':
                            if piece == Corner((C.YELLOW, C.BLUE, C.ORANGE)) and orientation == 2: continue
                        
                    # start cycle from this letter
                    letters.append(letter)
                    start_piece = piece
                    current_piece, current_orientation = piece, orientation
                    break
                else:
                    # if no new cycles can be started, algorithm is done
                    break
        
        return ''.join(letters)

    def M2_edges(self, new_cycle_order: str = 'ACWLJRTXVDB', parity: bool = False) -> str:
        '''Returns the sequence of letters for edges. New cycles are searched for in order of new_cycle_order'''
        letters: list[str] = []

        unsolved = {Edge((C.WHITE, C.GREEN)),
                    Edge((C.WHITE, C.RED)),
                    Edge((C.WHITE, C.BLUE)),
                    Edge((C.WHITE, C.ORANGE)),
                    Edge((C.GREEN, C.ORANGE)),
                    Edge((C.GREEN, C.RED)),
                    Edge((C.BLUE, C.RED)),
                    Edge((C.BLUE, C.ORANGE)),
                    Edge((C.YELLOW, C.GREEN)),
                    Edge((C.YELLOW, C.RED)),
                    Edge((C.YELLOW, C.BLUE)),
                    Edge((C.YELLOW, C.ORANGE))}
        
        current_piece, current_orientation = self.get_edge('U')
        start_piece = current_piece

        while True:
            next_letter = self.get_letter(current_piece, current_orientation, M2_parity=parity)
            next_piece, next_orientation = self.get_edge(next_letter)

            if next_piece != start_piece:
                letters.append(next_letter)
                unsolved.remove(next_piece)
                current_piece, current_orientation = next_piece, next_orientation
            else:
                if current_piece != Edge((C.YELLOW, C.GREEN)): # buffer piece
                    letters.append(next_letter)
                unsolved.remove(start_piece)

                # find new cycle
                for letter in new_cycle_order:
                    piece, orientation = self.get_edge(letter)
                    
                    # check if piece was solved by previous cycle
                    if piece not in unsolved:
                        continue
                    
                    # check if piece is already correct
                    match letter:
                        case 'A':
                            if not parity and piece == Edge((C.WHITE, C.BLUE)) and orientation == 0: continue
                            if parity and piece == Edge((C.WHITE, C.ORANGE)) and orientation == 0: continue
                        case 'Q':
                            if not parity and piece == Edge((C.WHITE, C.BLUE)) and orientation == 1: continue
                            if parity and piece == Edge((C.WHITE, C.ORANGE)) and orientation == 1: continue
                        case 'B':
                            if piece == Edge((C.WHITE, C.RED)) and orientation == 0: continue
                        case 'M':
                            if piece == Edge((C.WHITE, C.RED)) and orientation == 1: continue
                        case 'C':
                            if piece == Edge((C.WHITE, C.GREEN)) and orientation == 0: continue
                        case 'I':
                            if piece == Edge((C.WHITE, C.GREEN)) and orientation == 1: continue
                        case 'D':
                            if not parity and piece == Edge((C.WHITE, C.ORANGE)) and orientation == 0: continue
                            if parity and piece == Edge((C.WHITE, C.BLUE)) and orientation == 0: continue
                        case 'E':
                            if not parity and piece == Edge((C.WHITE, C.ORANGE)) and orientation == 1: continue
                            if parity and piece == Edge((C.WHITE, C.ORANGE)) and orientation == 1: continue
                        case 'L':
                            if piece == Edge((C.GREEN, C.ORANGE)) and orientation == 0: continue
                        case 'F':
                            if piece == Edge((C.GREEN, C.ORANGE)) and orientation == 1: continue
                        case 'J':
                            if piece == Edge((C.GREEN, C.RED)) and orientation == 0: continue
                        case 'P':
                            if piece == Edge((C.GREEN, C.RED)) and orientation == 1: continue
                        case 'T':
                            if piece == Edge((C.BLUE, C.RED)) and orientation == 0: continue
                        case 'N':
                            if piece == Edge((C.BLUE, C.RED)) and orientation == 1: continue
                        case 'R':
                            if piece == Edge((C.BLUE, C.ORANGE)) and orientation == 0: continue
                        case 'H':
                            if piece == Edge((C.BLUE, C.ORANGE)) and orientation == 1: continue
                        case 'U':
                            if piece == Edge((C.YELLOW, C.GREEN)) and orientation == 0: continue
                        case 'K':
                            if piece == Edge((C.YELLOW, C.GREEN)) and orientation == 1: continue
                        case 'V':
                            if piece == Edge((C.YELLOW, C.RED)) and orientation == 0: continue
                        case 'O':
                            if piece == Edge((C.YELLOW, C.RED)) and orientation == 1: continue
                        case 'W':
                            if piece == Edge((C.YELLOW, C.BLUE)) and orientation == 0: continue
                        case 'S':
                            if piece == Edge((C.YELLOW, C.BLUE)) and orientation == 1: continue
                        case 'X':
                            if piece == Edge((C.YELLOW, C.ORANGE)) and orientation == 0: continue
                        case 'G':
                            if piece == Edge((C.YELLOW, C.ORANGE)) and orientation == 1: continue
                        
                    # start cycle from this letter
                    letters.append(letter)
                    start_piece = piece
                    current_piece, current_orientation = piece, orientation
                    break
                else:
                    # if no new cycles can be started, algorithm is done
                    break
        
        return ''.join(letters)

    def __str__(self):
        return str(self.pieces)

    def make_moves(self, moves: str):
        '''Space separated sequence of moves'''
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
        '''Given a letter, returns what edge is at the letter and with what orientation'''
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
        '''Given a letter, returns what corner is at the letter and with what orientation'''
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

    def get_letter(self, *args: tuple[Corner | Edge, int] | tuple[tuple[Corner | Edge, int]], M2_parity: bool = False) -> str:
        '''Given a piece and orientation, returns the letter that the sticker should be at'''
        if len(args) == 1:
            piece, orientation = args[0]
        elif len(args) == 2:
            piece, orientation = args
        else:
            raise ValueError
        
        if isinstance(piece, Corner):
            match piece:
                case Corner((C.WHITE, C.ORANGE, C.BLUE)):
                    return 'A' if orientation == 0 else 'E' if orientation == 1 else 'R'
                case Corner((C.WHITE, C.BLUE, C.RED)):
                    return 'B' if orientation == 0 else 'Q' if orientation == 1 else 'N'
                case Corner((C.WHITE, C.RED, C.GREEN)):
                    return 'C' if orientation == 0 else 'M' if orientation == 1 else 'J'
                case Corner((C.WHITE, C.GREEN, C.ORANGE)):
                    return 'D' if orientation == 0 else 'I' if orientation == 1 else 'F'
                case Corner((C.YELLOW, C.ORANGE, C.GREEN)):
                    return 'U' if orientation == 0 else 'G' if orientation == 1 else 'L'
                case Corner((C.YELLOW, C.GREEN, C.RED)):
                    return 'V' if orientation == 0 else 'K' if orientation == 1 else 'P'
                case Corner((C.YELLOW, C.RED, C.BLUE)):
                    return 'W' if orientation == 0 else 'O' if orientation == 1 else 'T'
                case Corner((C.YELLOW, C.BLUE, C.ORANGE)):
                    return 'X' if orientation == 0 else 'S' if orientation == 1 else 'H'
        elif isinstance(piece, Edge):
            match piece:
                case Edge((C.WHITE, C.BLUE)):
                    return ('A' if orientation == 0 else 'Q') if not M2_parity else ('D' if orientation == 0 else 'E')
                case Edge((C.WHITE, C.RED)):
                    return 'B' if orientation == 0 else 'M'
                case Edge((C.WHITE, C.GREEN)):
                    return 'C' if orientation == 0 else 'I'
                case Edge((C.WHITE, C.ORANGE)):
                    return ('D' if orientation == 0 else 'E') if not M2_parity else ('A' if orientation == 0 else 'Q')
                case Edge((C.GREEN, C.ORANGE)):
                    return 'L' if orientation == 0 else 'F'
                case Edge((C.GREEN, C.RED)):
                    return 'J' if orientation == 0 else 'P'
                case Edge((C.BLUE, C.RED)):
                    return 'T' if orientation == 0 else 'N'
                case Edge((C.BLUE, C.ORANGE)):
                    return 'R' if orientation == 0 else 'H'
                case Edge((C.YELLOW, C.GREEN)):
                    return 'U' if orientation == 0 else 'K'
                case Edge((C.YELLOW, C.RED)):
                    return 'V' if orientation == 0 else 'O'
                case Edge((C.YELLOW, C.BLUE)):
                    return 'W' if orientation == 0 else 'S'
                case Edge((C.YELLOW, C.ORANGE)):
                    return 'X' if orientation == 0 else 'G'
