from src.configuration.constants import ConfigType, ConfigKeys
from src.modles.modles import Location
from src.utils.config_manager import ConfigManager


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        self.color: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.SNAKE_COLOR)
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.food_eaten: int = 0
        self.y_dir: int = 0
        self.x_dir: int = 0
        self.width: int = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.SNAKE_WIDTH_PX
        )
        self.height: int = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.SNAKE_HEIGHT_PX
        )

    def get_location(self) -> Location:
        return self.x_pos, self.y_pos

    def update_location(self, location: Location) -> None:
        self.x_pos = location[0]
        self.y_pos = location[1]

    def increase_food_eaten(self) -> None:
        self.food_eaten += 1
