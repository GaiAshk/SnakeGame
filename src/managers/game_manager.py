from src.configuration.constants import ConfigKeys, ConfigType
from src.contracts.game_contract import GameLib
from src.deps_wrappers.pygame_wrapper import Pygame
from src.utils.config_manager import ConfigManager


class GameManager:

    def __init__(
        self,
        game_lib: GameLib,
        screen_width_px: int,
        screen_height_px: int,
        screen_color: str,
    ):
        self.game_lib = game_lib
        self.delta_time: float = 0.0
        self.screen_width_px: int = screen_width_px
        self.screen_height_px: int = screen_height_px
        self.screen_color: str = screen_color

    def init_game(self):
        self.game_lib.init_game(
            self.screen_width_px, self.screen_height_px, self.screen_color
        )

        game_title = ConfigManager.get(ConfigType.GAME, ConfigKeys.GAME_TITLE)
        self.game_lib.set_screen_title(game_title)

    def update_clock(self) -> None:
        self.delta_time = self.game_lib.update_clock(
            ConfigManager.get_int(ConfigType.GAME, ConfigKeys.FPS)
        )

    def update_screen(self):
        self.game_lib.update_screen()

    def exit_game(self):
        self.game_lib.exit_game()

    def clean_screen(self):
        self.game_lib.clean_screen()

    def should_quit(self) -> bool:
        return self.game_lib.should_quit()
