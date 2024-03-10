from src.configuration.constants import ConfigKeys, ConfigType
from src.modles.modles import AllowedPlayerMoves, Location
from src.managers.drawing_manager import DrawingManager
from src.shapes.snake import Snake
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger


class SnakeManager:

    SNAKE_VALID_MOVE_BOARDER_PX = 7

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

    def update_location(
        self, player_move: AllowedPlayerMoves, delta_time: float
    ) -> None:
        if not self._is_move_valid(player_move, delta_time):
            return None

        self.snake.update_tail(self.snake.head_x_pos, self.snake.head_y_pos)
        logger.debug(f"Snake tail: {self.snake.tail}")

        self._update_snake_location_by_users_move(player_move, delta_time)

        logger.debug(
            f"Snake location is: {self.snake.head_y_pos}, {self.snake.head_x_pos}"
        )
        return None

    def get_current_snake_location(self) -> Location:
        return self.snake.head_x_pos, self.snake.head_y_pos

    def draw_snake(self) -> None:
        self.drawing_manager.draw_rect(
            self.snake.head_color,
            self.snake.head_x_pos,
            self.snake.head_y_pos,
            self.snake.width,
            self.snake.height,
        )

        for x, y in self.snake.tail:
            self.drawing_manager.draw_rect(
                self.snake.color,
                x,
                y,
                self.snake.width,
                self.snake.height,
            )

    def _is_move_valid(
        self, player_move: AllowedPlayerMoves, delta_time: float
    ) -> bool:
        """Checks if the move is valid, for example moving up when snake is at the top of the screen is not allowed
        because that will cause the snake to exit the screen"""
        key_movement_px = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.KEY_MOVEMENT_PX
        )
        border_px_y = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.BORDER_PX_Y)
        valid_move_boarder_y_px = border_px_y - self.SNAKE_VALID_MOVE_BOARDER_PX

        border_px_x = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.BORDER_PX_X)
        valid_move_boarder_x_px = border_px_x - self.SNAKE_VALID_MOVE_BOARDER_PX

        if player_move == player_move.up:
            new_y_pos = self.snake.head_y_pos - int(key_movement_px * delta_time)
            return False if new_y_pos - valid_move_boarder_y_px < 0 else True
        elif player_move == player_move.down:
            new_y_pos = self.snake.head_y_pos + int(key_movement_px * delta_time)
            return (
                False
                if new_y_pos + valid_move_boarder_y_px > self.screen_height_px
                else True
            )
        elif player_move == player_move.left:
            new_x_pos = self.snake.head_x_pos - int(key_movement_px * delta_time)
            return False if new_x_pos - valid_move_boarder_x_px < 0 else True
        elif player_move == player_move.right:
            new_x_pos = self.snake.head_x_pos + int(key_movement_px * delta_time)
            return (
                False
                if new_x_pos + valid_move_boarder_x_px > self.screen_width_px
                else True
            )
        elif player_move == player_move.no_move:
            pass
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
            self.snake.head_y_pos -= int(key_movement_px * delta_time)
        elif player_move == player_move.down:
            self.snake.x_dir = 0
            self.snake.y_dir = -1
            self.snake.head_y_pos += int(key_movement_px * delta_time)
        elif player_move == player_move.left:
            self.snake.x_dir = -1
            self.snake.y_dir = 0
            self.snake.head_x_pos -= int(key_movement_px * delta_time)
        elif player_move == player_move.right:
            self.snake.x_dir = 1
            self.snake.y_dir = 0
            self.snake.head_x_pos += int(key_movement_px * delta_time)
        elif player_move == player_move.no_move:
            # continue to move the same direction the same was moving in for the last time
            if self.snake.x_dir != 0:
                self.snake.head_x_pos += int(
                    key_movement_px * delta_time * self.snake.x_dir
                )
            elif self.snake.y_dir != 0:
                self.snake.head_y_pos -= int(
                    key_movement_px * delta_time * self.snake.y_dir
                )
            else:
                logger.error("un expected result, snake direction must be x or y")
        else:
            logger.error("Not allowed move")

    def snake_ate_food(self) -> None:
        self.snake.increase_food_eaten()

    def _is_snake_hitting_boarder(self) -> bool:
        border_y_px = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.BORDER_PX_Y)
        border_x_px = ConfigManager.get_int(ConfigType.GAME, ConfigKeys.BORDER_PX_X)

        if self.snake.head_y_pos - border_y_px <= 0:
            return True

        if self.snake.head_y_pos + border_y_px >= self.screen_height_px:
            return True

        if self.snake.head_x_pos + border_x_px >= self.screen_width_px:
            return True

        if self.snake.head_x_pos - border_x_px <= 0:
            return True

        return False

    def is_snake_dead(self) -> bool:
        is_snake_on_himself: bool = (
            self.snake.head_x_pos,
            self.snake.head_y_pos,
        ) in self.snake.tail
        if is_snake_on_himself:
            logger.info(
                f"Snake on himself, snake position: {self.snake.head_x_pos}, {self.snake.head_y_pos}"
            )

        is_snake_on_boarder: bool = self._is_snake_hitting_boarder()
        if is_snake_on_boarder:
            logger.info(
                f"Snake on boarder, snake position: {self.snake.head_x_pos}, {self.snake.head_y_pos}"
            )

        return is_snake_on_himself or is_snake_on_boarder

    def kill_snake(self) -> None:
        snake_initial_x_position, snake_initial_y_position = (
            self.drawing_manager.get_screen_center()
        )
        self.snake = Snake(snake_initial_x_position, snake_initial_y_position)

    def get_food_eaten(self) -> int:
        return self.snake.food_eaten
