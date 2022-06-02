import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
	col_pins = (board.A3, board.A2, board.A1, board.A0, board.D10, board.D9)
	row_pins = (board.D2, board.D3, board.D4, board.D5, board.D6, board.D7)    #black on 1n4148 towards rows
	diode_orientation = DiodeOrientation.ROW2COL

    # New coord_mapping is to the code layout in code.py. In order to map it correctly, it must be in the same layout.
	coord_mapping = [
     0,  1,  2,  3,  4,  5,  41, 40, 39, 38, 37, 36,
     6,  7,  8,  9, 10, 11,  47, 46, 45, 44, 43, 42,
    12, 13, 14, 15, 16, 17,  53, 52, 51, 50, 49, 48,
    18, 19, 20, 21, 22, 23,  59, 58, 57, 56, 55, 54,
            26, 27,                  63, 62,
                28, 29,          65, 64,
                    34, 35,  71, 70, 
                    32, 33,  69, 68,
    ]