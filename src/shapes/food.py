from src.configuration.constants import ConfigType, ConfigKeys
from src.utils.config_manager import ConfigManager


class Food:
    def __init__(self) -> None:
        self.color = ConfigManager.get(ConfigType.GAME, ConfigKeys.FOOD_COLOR)
        self.x_pos: int = 0
        self.y_pos: int = 0

    def create_food(self):
        pass
