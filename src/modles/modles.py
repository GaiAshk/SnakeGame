from enum import Enum
from typing import Tuple


class AllowedPlayerMoves(Enum):
    no_move = 0
    up = 1
    down = 2
    left = 3
    right = 4


class AllowedDrawingLibs(Enum):
    pygame = "pygame"
    turtle = "turtle"


class AllowedGameLibs(Enum):
    pygame = "pygame"
    turtle = "turtle"


Location = tuple[int, int]  # location[0] is x-axis and location[1] is y-axis
