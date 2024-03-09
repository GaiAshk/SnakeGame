from abc import ABC, abstractmethod
from typing import Any

from src.configuration.constants import ConfigKeys, ConfigType
from src.modles.modles import AllowedGameLibs, AllowedPlayerMoves
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger


class GameLib(ABC):

    @abstractmethod
    def init_game(self, screen_width_px: int, screen_height_px: int, screen_color: str):
        pass

    @abstractmethod
    def set_screen_title(self, title: str) -> None:
        pass

    @abstractmethod
    def update_clock(self, fps: int) -> float:
        pass

    @abstractmethod
    def update_screen(self) -> None:
        pass

    @abstractmethod
    def exit_game(self):
        pass

    @abstractmethod
    def clean_screen(self):
        pass

    @abstractmethod
    def should_quit(self) -> bool:
        pass

    @abstractmethod
    def display_score(self, score: str):
        pass

    @abstractmethod
    def get_players_move(self) -> AllowedPlayerMoves:
        pass


def get_game_lib() -> GameLib | Any:
    game_lib: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.GAME_LIB)
    if game_lib == AllowedGameLibs.pygame.value:
        from src.deps_wrappers.pygame_wrapper import Pygame

        return Pygame
    elif game_lib == AllowedGameLibs.turtle.value:
        from src.deps_wrappers.turtle_wrapper import TurtleWrap

        return TurtleWrap
    else:
        logger.error("invalid drawing lib")
        return None
