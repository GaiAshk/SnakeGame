from src.configuration.allowed_player_moves import AllowedPlayerMoves
from src.configuration.constants import ConfigType, ConfigKeys
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        self.color: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.SNAKE_COLOR)
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.food_eaten: int = 0
        self.y_dir: int = 0
        self.x_dir: int = 0
        self.width: int = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.SNAKE_WIDTH_PX)
        self.height: int = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.SNAKE_HEIGHT_PX)

    def calc_snake_next_move(self):
        pass

    def update_location(self, player_move: AllowedPlayerMoves, delta_time: float) -> None:
        key_movement_px = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.KEY_MOVEMENT_PX)
        if player_move.no_move:
            logger.info("No move made")
            return None
        elif player_move.up:
            self.x_dir = 0
            self.y_dir = 1
            self.y_pos -= (key_movement_px * delta_time)
        elif player_move.down:
            self.x_dir = 0
            self.y_dir = -1
            self.y_pos += (key_movement_px * delta_time)
        elif player_move.left:
            self.x_dir = -1
            self.y_dir = 0
            self.x_pos -= (key_movement_px * delta_time)
        elif player_move.right:
            self.x_dir = 1
            self.y_dir = 0
            self.x_pos += (key_movement_px * delta_time)
        else:
            logger.error("Not allowed move")

        logger.debug(f"Snake location is: {self.y_pos}, {self.x_pos}")
        return None