from src.configuration.constants import ConfigType, ConfigKeys
from src.modles.modles import Location
from src.utils.config_manager import ConfigManager


class Food:
    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        self.color: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.FOOD_COLOR)
        self.radius: int = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.FOOD_RADIUS
        )
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos

    def get_location(self) -> Location:
        return self.x_pos, self.y_pos

    def update_location(self, location: Location) -> None:
        self.x_pos = location[0]
        self.y_pos = location[1]
