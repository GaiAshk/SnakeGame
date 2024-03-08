from src.configuration.modles import Location
from src.contracts.drawing_contract import DrawingLib, DrawLibTyping


class DrawingManager:

    def __init__(self, drawing_lib: DrawingLib = DrawLibTyping()):
        self.drawing_lib: DrawingLib = drawing_lib

    def update_drawing_manager(self, drawing_lib: DrawingLib):
        self.drawing_lib = drawing_lib

    def draw_circle(self, color: str, center: Location, radius: int) -> None:
        self.drawing_lib.draw_circle(color, center, radius)

    def draw_rect(
        self, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        self.drawing_lib.draw_rect(color, left, top, width, height)
