import turtle

from src.modles.modles import AllowedPlayerMoves
from src.contracts.drawing_contract import DrawingLib
from src.contracts.game_contract import GameLib


class TurtleWrap(DrawingLib, GameLib):

    screen = turtle.Screen()
    screen_width_px: int = 700
    screen_height_px: int = 700

    @classmethod
    def init(cls):
        pass

    @classmethod
    def set_screen_title(cls, title: str) -> None:
        screen = turtle.Screen()
        screen.title(title)

    @classmethod
    def display_score(cls, score_txt: str):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(10, 10)
        pen.write(score_txt, align="center", font=("candara", 36, "bold"))

    @classmethod
    def set_screen_mode(
        cls, screen_width_px: int, screen_height_px: int, screen_color: str
    ) -> None:
        cls.screen_width_px = screen_width_px
        cls.screen_height_px = screen_height_px

        cls.screen.setup(width=screen_width_px, height=screen_height_px)
        cls.screen.bgcolor(screen_color)

    @classmethod
    def init_game(cls, screen_width_px: int, screen_height_px: int, screen_color: str):
        pass

    @classmethod
    def init_clock(cls):
        pass

    @classmethod
    def event_get(cls):
        pass

    @classmethod
    def should_quit(cls) -> bool:
        pass

    @classmethod
    def clean_screen(cls):
        turtle.clearscreen()

    @classmethod
    def exit_game(cls):
        turtle.bye()

    @classmethod
    def update_screen(cls):
        cls.screen.update()

    @classmethod
    def draw_rect(
        cls, color: str, left: int, top: int, width: int, height: int
    ) -> None:
        rect = turtle.Turtle()
        rect.shape("square")
        rect.color(color)
        rect.penup()

    @classmethod
    def draw_circle(cls, color: str, center: tuple[int, int], radius: int):
        food = turtle.Turtle()
        food.speed(0)
        food.circle(radius)
        food.color(color)
        food.penup()
        food.goto(center[0], center[1])

    @classmethod
    def update_clock(cls, fps: int) -> float:
        return 1.0

    @classmethod
    def get_screen_center(cls) -> tuple[int, int]:
        return int(cls.screen_width_px / 2), int(cls.screen_height_px / 2)

    @classmethod
    def get_players_move(cls) -> AllowedPlayerMoves:
        cls.screen.listen()

        player_move = AllowedPlayerMoves.no_move

        def go_up():
            nonlocal player_move
            player_move = AllowedPlayerMoves.up

        def go_down():
            nonlocal player_move
            player_move = AllowedPlayerMoves.down

        def go_left():
            nonlocal player_move
            player_move = AllowedPlayerMoves.left

        def go_right():
            nonlocal player_move
            player_move = AllowedPlayerMoves.right

        cls.screen.onkeypress(go_up, "w")
        cls.screen.onkeypress(go_down, "s")
        cls.screen.onkeypress(go_right, "d")
        cls.screen.onkeypress(go_left, "a")

        return player_move
