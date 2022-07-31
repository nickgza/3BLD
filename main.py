from enums import Colour, Face, Move
from cube import Cube
import numpy as np

index = 1

test_cube = Cube()
# test_cube.make_moves("U")
# test_cube.make_move("F")
test_cube.make_moves("U R' F2 U2 D L' D' L")
print(test_cube.get_edge('U'))
print(test_cube.get_letter(test_cube.get_edge('U')))
