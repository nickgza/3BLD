from enums import Colour as C, Face as F, Move
from cube import Cube
import numpy as np

test = Cube()

scramble = "D2 L' B L U F' L2 U'"

test.make_moves(scramble)
print(test.pochmann_corners())
