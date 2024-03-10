from src.configuration.constants import ConfigType, ConfigKeys
from src.modles.modles import Location
from src.utils.config_manager import ConfigManager


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        self.color: str = ConfigManager.get(ConfigType.GAME, ConfigKeys.SNAKE_COLOR)
        self.head_color: str = ConfigManager.get(
            ConfigType.GAME, ConfigKeys.SNAKE_HEAD_COLOR
        )
        self.head_x_pos: int = x_pos
        self.head_y_pos: int = y_pos
        self.food_eaten: int = 0
        self.y_dir: int | float = 0.1
        self.x_dir: int = 0
        self.width: int = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.SNAKE_WIDTH_PX
        )
        self.height: int = ConfigManager.get_int(
            ConfigType.GAME, ConfigKeys.SNAKE_HEIGHT_PX
        )
        self.tail: list[Location] = (
            []
        )  # the list of locations showing the tail of the snake, where the location in
        # the Nth position is the oldest snake position, not the head

    def get_location(self) -> Location:
        return self.head_x_pos, self.head_y_pos

    def update_location(self, location: Location) -> None:
        self.head_x_pos = location[0]
        self.head_y_pos = location[1]

    def increase_food_eaten(self) -> None:
        self.food_eaten += 1
        self.tail.append((self.head_x_pos, self.head_y_pos))

    def update_tail(self, snake_x_pos: int, snake_y_pos: int) -> None:
        n = len(self.tail)
        if n < 1:
            return None

        for i in range(n):
            if i == 0:
                continue

            self.tail[n - i] = self.tail[n - i - 1]

        self.tail[0] = snake_x_pos, snake_y_pos
        return None
