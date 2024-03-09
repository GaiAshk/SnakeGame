from src.modles.modles import Location
from src.configuration.constants import ConfigType, ConfigKeys
from src.contracts.drawing_contract import DrawingLib, get_drawing_lib
from src.contracts.game_contract import GameLib, get_game_lib
from src.managers.drawing_manager import DrawingManager
from src.managers.food_manager import FoodManager
from src.managers.game_manager import GameManager
from src.managers.player_manager import PlayerManager
from src.managers.snake_manager import SnakeManager
from src.utils.config_manager import ConfigManager
from src.utils.intersections import do_location_intersect
from src.utils.logger import logger

drawing_lib: DrawingLib = get_drawing_lib()
drawing_manager: DrawingManager = DrawingManager(drawing_lib)

game_lib: GameLib = get_game_lib()
screen_width_px: int = ConfigManager.get_int(
    ConfigType.SCREEN, ConfigKeys.SCREEN_WIDTH_PX
)
screen_height_px: int = ConfigManager.get_int(
    ConfigType.SCREEN, ConfigKeys.SCREEN_HEIGHT_PX
)
screen_color: str = ConfigManager.get(ConfigType.SCREEN, ConfigKeys.SCREEN_COLOR)
game_manager: GameManager = GameManager(
    game_lib, screen_width_px, screen_height_px, screen_color
)

snake_manager: SnakeManager = SnakeManager(
    screen_width_px, screen_height_px, drawing_manager
)
food_manager: FoodManager = FoodManager(
    screen_width_px, screen_height_px, drawing_manager
)


def draw_snake() -> None:
    player_move = PlayerManager.get_player_move()
    snake_manager.update_location(player_move, game_manager.delta_time)
    snake_manager.draw_snake()


def draw_food_and_snake_ate_food_logic():
    if is_food_eaten():
        logger.info("updating food location")
        food_manager.update_food_location()
        snake_manager.snake_ate_food()
    else:
        food_manager.draw_food()


def init_game():
    game_manager.init_game()


def _does_snake_intersect_with_food(
    food_location: Location, snake_location: Location
) -> bool:
    food_eating_sensitivity: int = ConfigManager.get_int(
        ConfigType.GAME, ConfigKeys.FOOD_EATING_SENSITIVITY
    )
    return do_location_intersect(food_location, snake_location, food_eating_sensitivity)


def is_food_eaten() -> bool:
    current_food_location: Location = food_manager.get_food_location()
    current_snake_location: Location = snake_manager.get_current_snake_location()

    if _does_snake_intersect_with_food(current_food_location, current_snake_location):
        return True
    else:
        return False


def check_if_snake_died() -> bool:
    return snake_manager.is_snake_dead()


def display_score():
    game_manager.display_score(snake_manager.get_food_eaten())


def run_game():
    init_game()

    running = True

    while running:
        if game_manager.should_quit():
            running = False

        game_manager.clean_screen()

        display_score()

        draw_snake()

        if check_if_snake_died():
            logger.info("Snake died, restarting game...")
            snake_manager.kill_snake()

        draw_food_and_snake_ate_food_logic()

        game_manager.update_screen()

        game_manager.update_clock()

    game_manager.exit_game()
