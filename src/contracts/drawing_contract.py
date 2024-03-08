from abc import ABC, abstractmethod
from typing import Any, Union

from src.configuration.constants import ConfigKeys, ConfigType
from src.configuration.modles import AllowedDrawingLibs
from src.utils.config_manager import ConfigManager
from src.utils.logger import logger


class DrawingLib(ABC):

    @abstractmethod
    def draw_circle(self, color: str, center: tuple[int, int], radius: int) -> None:
        pass

    @abstractmethod
    def draw_rect(
        self, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        pass

    @abstractmethod
    def get_screen_center(self):
        pass


class DrawLibTyping(DrawingLib):
    def draw_circle(self, color: str, center: tuple[int, int], radius: int) -> None:
        pass

    def draw_rect(
        self, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        pass

    def get_screen_center(self):
        pass


def get_drawing_lib() -> Union[DrawingLib, Any]:
    drawing_lib: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.DRAWING_LIB)
    if drawing_lib == AllowedDrawingLibs.pygame.value:
        from src.deps_wrappers.pygame_wrapper import Pygame

        return Pygame
    else:
        logger.error("invalid drawing lib")
        return None
