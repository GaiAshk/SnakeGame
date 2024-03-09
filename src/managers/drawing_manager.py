from src.modles.modles import Location
from src.contracts.drawing_contract import DrawingLib


class DrawingManager:

    def __init__(self, drawing_lib: DrawingLib):
        self.drawing_lib: DrawingLib = drawing_lib

    def draw_circle(self, color: str, center: Location, radius: int) -> None:
        self.drawing_lib.draw_circle(color, center, radius)

    def draw_rect(
        self, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        self.drawing_lib.draw_rect(color, left, top, width, height)

    def get_screen_center(self) -> tuple[int, int]:
        screen_center_x, screen_center_y = self.drawing_lib.get_screen_center()
        return screen_center_x, screen_center_y
