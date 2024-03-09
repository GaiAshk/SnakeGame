from abc import ABC, abstractmethod
from typing import Any, Union

from src.configuration.constants import ConfigKeys, ConfigType
from src.modles.modles import AllowedDrawingLibs
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


def get_game_lib() -> Union[GameLib, Any]:
    game_lib: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.GAME_LIB)
    if game_lib == AllowedDrawingLibs.pygame.value:
        from src.deps_wrappers.pygame_wrapper import Pygame

        return Pygame
    else:
        logger.error("invalid drawing lib")
        return None
