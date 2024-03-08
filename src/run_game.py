from src.configuration.modles import AllowedPlayerMoves, Location
from src.configuration.constants import ConfigType, ConfigKeys
from src.contracts.drawing_contract import DrawingLib, get_drawing_lib
from src.deps_wrappers.pygame_wrapper import Pygame
from src.managers.drawing_manager import DrawingManager
from src.managers.food_manager import FoodManager
from src.shapes.snake import Snake
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger
from typing import Optional

snake: Optional[Snake] = None
drawing_manager: DrawingManager = DrawingManager()
food_manager: FoodManager = FoodManager(0, 0, drawing_manager)
delta_time: float = 0.0


def draw_snake() -> None:
    global snake
    if not snake:
        # draw first snake at screen center
        screen_center_x, screen_center_y = Pygame.get_screen_center()
        snake = Snake(screen_center_x, screen_center_y)
        Pygame.draw_rect(
            snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height
        )
        return None

    # update snake location
    player_move = get_player_move()

    snake.update_location(player_move, delta_time)

    Pygame.draw_rect(snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height)


def get_player_move() -> AllowedPlayerMoves:
    return Pygame.get_players_move()


def create_food():
    screen_width_px = ConfigManager.get_int(
        ConfigType.SCREEN, ConfigKeys.SCREEN_WIDTH_PX
    )
    screen_height_px = ConfigManager.get_int(
        ConfigType.SCREEN, ConfigKeys.SCREEN_HEIGHT_PX
    )

    global food_manager
    if not food_manager.is_initialized():
        food_manager.re_init(screen_width_px, screen_height_px, drawing_manager)

    if is_food_eaten():
        logger.info("updating food location")
        food_manager.update_food_location()
    else:
        food_manager.draw_food()


def pre_init() -> None:
    drawing_lib: DrawingLib = get_drawing_lib()
    drawing_manager.update_drawing_manager(drawing_lib)


def update_clock():
    global delta_time
    delta_time = Pygame.tick_clock(
        ConfigManager.get_int(ConfigType.GAME, ConfigKeys.FPS)
    )


def init_game():
    Pygame.init()

    screen_width_px = ConfigManager.get_int(
        ConfigType.SCREEN, ConfigKeys.SCREEN_WIDTH_PX
    )
    screen_height_px = ConfigManager.get_int(
        ConfigType.SCREEN, ConfigKeys.SCREEN_HEIGHT_PX
    )
    screen_color = ConfigManager.get(ConfigType.SCREEN, ConfigKeys.SCREEN_COLOR)
    Pygame.set_screen_mode(screen_width_px, screen_height_px, screen_color)


def is_food_eaten() -> bool:
    current_food_location: Location = food_manager.food.get_food_location()
    current_snake_location: Location = snake.get_current_snake_location()

    if (
        current_food_location[0] == current_snake_location[0]
        and current_food_location[1] == current_snake_location[1]
    ):
        return True
    else:
        return False


def run_game():
    pre_init()

    init_game()

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
