from enums import Colour as C, Face as F, Move
from piece import Corner, Edge
import numpy as np
import string

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
