from src.configuration.modles import Location
from src.managers.drawing_manager import DrawingManager
from src.shapes.food import Food
from src.utils.random_number_generator import get_random_int


class FoodManager:

    def __init__(
        self,
        screen_width_px: int,
        screen_height_px: int,
        drawing_manager: DrawingManager,
    ) -> None:
        self.screen_width_px = screen_width_px
        self.screen_height_px = screen_height_px
        self.drawing_manager: DrawingManager = drawing_manager
        self.food: Food = Food()

    def is_initialized(self) -> bool:
        if self.screen_width_px == 0 or self.screen_height_px == 0:
            return False
        else:
            return True

    def re_init(
        self,
        screen_width_px: int,
        screen_height_px: int,
        drawing_manager: DrawingManager,
    ) -> None:
        self.screen_width_px = screen_width_px
        self.screen_height_px = screen_height_px
        self.drawing_manager = drawing_manager
        self.food.update_food_location(self._get_new_food_location())

    def _get_new_food_location(self) -> Location:
        food_x_px: int = get_random_int(0, self.screen_width_px)
        food_y_px: int = get_random_int(0, self.screen_height_px)
        return food_x_px, food_y_px

    def _draw_food(self, food_x_px: int, food_y_px: int) -> None:
        center: Location = food_x_px, food_y_px
        self.drawing_manager.draw_circle(self.food.color, center, self.food.radius)
        self.food.update_food_location(center)

    def draw_food(self):
        food_x_px, food_y_px = self.food.get_food_location()
        self._draw_food(food_x_px, food_y_px)

    def update_food_location(self):
        food_x_px, food_y_px = self._get_new_food_location()
        self._draw_food(food_x_px, food_y_px)
