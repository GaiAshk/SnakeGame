from src.configuration.constants import ConfigKeys, ConfigType
from src.configuration.modles import AllowedPlayerMoves, Location
from src.managers.drawing_manager import DrawingManager
from src.shapes.snake import Snake
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger


class SnakeManager:

    def __init__(
        self,
        screen_width_px: int,
        screen_height_px: int,
        drawing_manager: DrawingManager,
    ) -> None:
        self.screen_width_px = screen_width_px
        self.screen_height_px = screen_height_px
        self.drawing_manager: DrawingManager = drawing_manager

        snake_initial_x_position, snake_initial_y_position = (
            self.drawing_manager.get_screen_center()
        )
        self.snake: Snake = Snake(snake_initial_x_position, snake_initial_y_position)

    def calc_snake_next_move(self):
        pass

    def update_location(
        self, player_move: AllowedPlayerMoves, delta_time: float
    ) -> None:
        key_movement_px = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.KEY_MOVEMENT_PX
        )
        if player_move == player_move.no_move:
            return None
        elif player_move == player_move.up:
            self.snake.x_dir = 0
            self.snake.y_dir = 1
            self.snake.y_pos -= int(key_movement_px * delta_time)
        elif player_move == player_move.down:
            self.snake.x_dir = 0
            self.snake.y_dir = -1
            self.snake.y_pos += int(key_movement_px * delta_time)
        elif player_move == player_move.left:
            self.snake.x_dir = -1
            self.snake.y_dir = 0
            self.snake.x_pos -= int(key_movement_px * delta_time)
        elif player_move == player_move.right:
            self.snake.x_dir = 1
            self.snake.y_dir = 0
            self.snake.x_pos += int(key_movement_px * delta_time)
        else:
            logger.error("Not allowed move")

        logger.debug(f"Snake location is: {self.snake.y_pos}, {self.snake.x_pos}")
        return None

    def get_current_snake_location(self) -> Location:
        return self.snake.x_pos, self.snake.y_pos

    def draw_snake(self) -> None:
        self.drawing_manager.draw_rect(
            self.snake.color,
            self.snake.x_pos,
            self.snake.y_pos,
            self.snake.width,
            self.snake.height,
        )
