import pygame

from src.configuration.modles import AllowedPlayerMoves
from src.contracts.drawing_contract import DrawingLib


class Pygame(DrawingLib):

    screen: pygame.surface.Surface = pygame.display.set_mode((0, 0))
    screen_color: str = "no_color"
    clock: pygame.time.Clock = pygame.time.Clock()

    @classmethod
    def init(cls):
        pygame.init()

    @classmethod
    def set_screen_mode(cls, screen_width_px, screen_height_px, screen_color):
        cls.screen = pygame.display.set_mode((screen_width_px, screen_height_px))
        cls.screen_color = screen_color
        cls.screen.fill(screen_color)

    @classmethod
    def init_clock(cls) -> pygame.time.Clock:
        return pygame.time.Clock()

    @classmethod
    def event_get(cls):
        return pygame.event.get()

    @classmethod
    def should_quit(cls):
        for event in Pygame.event_get():
            if event.type == pygame.QUIT:
                return True
        return False

    @classmethod
    def wipe_screen(cls):
        cls.screen.fill(cls.screen_color)

    @classmethod
    def quit(cls):
        pygame.quit()

    @classmethod
    def flip(cls):
        pygame.display.flip()

    @classmethod
    def draw_rect(
        cls, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        pygame_rect: pygame.Rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(cls.screen, color, pygame_rect)

    @classmethod
    def draw_rect_move(cls, x: int, y: int):
        pass

    @classmethod
    def draw_circle(cls, color: str, center: tuple[int, int], radius: int):
        pygame.draw.circle(cls.screen, color, center, radius)

    @classmethod
    def tick_clock(cls, fps: int) -> float:
        # limits FPS to a constant FPS
        # dt is delta time in seconds since last frame, used for frame rate independent physics.
        dt: float = cls.clock.tick(fps) / 1000
        return dt

    @classmethod
    def get_screen_center(cls) -> tuple[int, int]:
        vector = cls.screen.get_width() / 2, cls.screen.get_height() / 2
        return int(vector[0]), int(vector[1])

    @classmethod
    def get_players_move(cls) -> AllowedPlayerMoves:
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            return AllowedPlayerMoves.up
        elif key[pygame.K_s]:
            return AllowedPlayerMoves.down
        elif key[pygame.K_a]:
            return AllowedPlayerMoves.left
        elif key[pygame.K_d]:
            return AllowedPlayerMoves.right
        else:
            return AllowedPlayerMoves.no_move
