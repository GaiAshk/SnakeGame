from src.configuration.allowed_player_moves import AllowedPlayerMoves
from src.configuration.constants import SNAKE_COLOR, KEY_MOVEMENT_PX, SNAKE_HEIGHT_PX, SNAKE_WIDTH_PX


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        self.color: str = SNAKE_COLOR
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.food_eaten: int = 0
        self.y_dir: int = 0
        self.x_dir: int = 0
        self.width: int = SNAKE_WIDTH_PX
        self.height: int = SNAKE_HEIGHT_PX

    def calc_snake_next_move(self):
        pass

    def update_location(self, player_move: AllowedPlayerMoves, delta_time: float) -> None:
        if player_move.no_move:
            print("No move made")
            return None
        elif player_move.up:
            self.x_dir = 0
            self.y_dir = 1
            self.y_pos -= (KEY_MOVEMENT_PX * delta_time)
        elif player_move.down:
            self.x_dir = 0
            self.y_dir = -1
            self.y_pos += (KEY_MOVEMENT_PX * delta_time)
        elif player_move.left:
            self.x_dir = -1
            self.y_dir = 0
            self.x_pos -= (KEY_MOVEMENT_PX * delta_time)
        elif player_move.right:
            self.x_dir = 1
            self.y_dir = 0
            self.x_pos += (KEY_MOVEMENT_PX * delta_time)
        else:
            print("Not allowed move")

        print(f"Snake location is: {self.y_pos}, {self.x_pos}")
        return None
