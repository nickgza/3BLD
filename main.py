from enums import Colour as C, Face as F, Move
from cube import Cube
import numpy as np

test = Cube()

print(scramble := test.generate_scramble())

test.make_moves(scramble)

corners_letters, edges_letters = test.pochmann_corners(), test.M2_edges()
print(' '.join(corners_letters[i:i+2] for i in range(0, len(corners_letters), 2)))
print(' '.join(edges_letters[i:i+2] for i in range(0, len(edges_letters), 2)))
