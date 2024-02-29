from src.configuration.allowed_player_moves import AllowedPlayerMoves
from src.configuration.constants import ConfigType, ConfigKeys
from src.deps_wrappers.pygame_wrapper import Pygame
from src.shapes.snake import Snake
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger
from typing import Optional

snake: Optional[Snake] = None
delta_time: float = 0.0


def draw_snake() -> None:
    logger.debug("Draw Snake")

    global snake
    if not snake:
        # draw first snake at screen center
        screen_center_x, screen_center_y = Pygame.get_screen_center()
        snake = Snake(screen_center_x, screen_center_y)
        Pygame.draw_rect(snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height)
        return None

    # update snake location
    player_move = get_player_move()
    snake.update_location(player_move, delta_time)
    Pygame.draw_rect(snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height)


def get_player_move() -> AllowedPlayerMoves:
    return Pygame.get_players_move()


def create_food():
    logger.info("create_food")
    pass


def update_clock():
    global delta_time
    delta_time = Pygame.tick_clock(ConfigManager.get_int(ConfigType.GAME, ConfigKeys.FPS))


def run_game():

    Pygame.init()

    screen_width_px = ConfigManager.get_int(ConfigType.SCREEN, ConfigKeys.SCREEN_WIDTH_PX)
    screen_height_px = ConfigManager.get_int(ConfigType.SCREEN, ConfigKeys.SCREEN_HEIGHT_PX)
    screen_color = ConfigManager.get(ConfigType.SCREEN, ConfigKeys.SCREEN_COLOR)
    Pygame.set_screen_mode(screen_width_px, screen_height_px, screen_color)

    Pygame.init_clock()

    running = True

    while running:
        if Pygame.should_quit():
            running = False

        Pygame.wipe_screen()

        draw_snake()

        create_food()

        Pygame.flip()

        update_clock()

    Pygame.quit()
