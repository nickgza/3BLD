from enums import Colour as C, Face as F, Move
from cube import Cube
import numpy as np

test = Cube()

scramble = "U2 B2 R' U2 R F2 B2 U2 R2 D' L' B' L F D R' L2 U B' L' D' R U F' B'"

test.make_moves(scramble)
print(test.pochmann_corners())
print(test.M2_edges())
