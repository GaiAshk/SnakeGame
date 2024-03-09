from src.configuration.constants import ConfigKeys, ConfigType
from src.modles.modles import AllowedPlayerMoves, Location
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
        if not self._is_move_valid(player_move, delta_time):
            return None

        self._update_snake_location_by_users_move(player_move, delta_time)

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

    def _is_move_valid(
        self, player_move: AllowedPlayerMoves, delta_time: float
    ) -> bool:
        """Checks if the move is valid, for example moving up when snake is at the top of the screen is not allowed
        because that will cause the snake to exit the screen"""
        if player_move == player_move.no_move:
            return False

        key_movement_px = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.KEY_MOVEMENT_PX
        )
        border_px = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.BORDER_PX)

        if player_move == player_move.up:
            new_y_pos = self.snake.y_pos - int(key_movement_px * delta_time)
            return False if new_y_pos - border_px < 0 else True
        elif player_move == player_move.down:
            new_y_pos = self.snake.y_pos + int(key_movement_px * delta_time)
            return False if new_y_pos + border_px > self.screen_height_px else True
        elif player_move == player_move.left:
            new_x_pos = self.snake.x_pos - int(key_movement_px * delta_time)
            return False if new_x_pos - border_px < 0 else True
        elif player_move == player_move.right:
            new_x_pos = self.snake.x_pos + int(key_movement_px * delta_time)
            return False if new_x_pos + border_px > self.screen_width_px else True
        else:
            logger.error("invalid move check")
        return True

    def _update_snake_location_by_users_move(
        self, player_move: AllowedPlayerMoves, delta_time: float
    ) -> None:
        key_movement_px = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.KEY_MOVEMENT_PX
        )

        if player_move == player_move.up:
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
