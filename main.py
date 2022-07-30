from enums import Colour, Face, Move
from cube import Cube
import numpy as np

index = 1

test_cube = Cube()
# test_cube.make_moves("U")
# test_cube.make_move("F")
test_cube.make_moves("B L2 R2 B' U2 R2 D' U' F R2 D' B F' U B U L' F' U2 L' R2 F R' B2 D U2 R B2 F' D'")
print(test_cube)
