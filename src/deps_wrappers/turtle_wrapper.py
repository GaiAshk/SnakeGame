import turtle

from src.modles.modles import AllowedPlayerMoves
from src.contracts.drawing_contract import DrawingLib
from src.contracts.game_contract import GameLib


class TurtleWrap(DrawingLib, GameLib):

    screen = turtle.Screen()
    screen.tracer(0)
    screen_width_px: int = 700
    screen_height_px: int = 700
    screen_background_color: str = "black"

    player_move = AllowedPlayerMoves.no_move

    # @classmethod
    # def go_up(cls):
    #     print("go up called")
    #     cls.player_move = AllowedPlayerMoves.up
    #
    # @classmethod
    # def go_down(cls):
    #     print("go up called")
    #     cls.player_move = AllowedPlayerMoves.down
    #
    # @classmethod
    # def go_left(cls):
    #     print("go up called")
    #     cls.player_move = AllowedPlayerMoves.left
    #
    # @classmethod
    # def go_right(cls):
    #     print("go up called")
    #     cls.player_move = AllowedPlayerMoves.right
    #
    # screen.listen()
    # screen.onkeypress(go_up, "w")
    # screen.onkeypress(go_down, "s")
    # screen.onkeypress(go_right, "d")
    # screen.onkeypress(go_left, "a")

    @classmethod
    def init(cls):
        pass

    @classmethod
    def set_screen_title(cls, title: str) -> None:
        cls.screen.title(title)

    @classmethod
    def display_score(cls, score_txt: str):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.setposition(
            cls._shift_x_int_to_turtle_screen(60), cls._shift_y_int_to_turtle_screen(40)
        )
        pen.write(score_txt, align="center", font=("candara", 24, "bold"))

    @classmethod
    def set_screen_mode(
        cls, screen_width_px: int, screen_height_px: int, screen_color: str
    ) -> None:
        cls.screen_width_px = screen_width_px
        cls.screen_height_px = screen_height_px
        cls.screen_background_color = screen_color

        cls.screen.setup(width=screen_width_px, height=screen_height_px)
        cls.screen.bgcolor(cls.screen_background_color)

    @classmethod
    def init_game(cls, screen_width_px: int, screen_height_px: int, screen_color: str):
        cls.set_screen_mode(screen_width_px, screen_height_px, screen_color)

    @classmethod
    def init_clock(cls):
        pass

    @classmethod
    def should_quit(cls) -> bool:
        return False

    @classmethod
    def clean_screen(cls):
        turtle.clearscreen()
        cls.screen.bgcolor(cls.screen_background_color)

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
        rect.speed(0)

        rect.setposition(
            cls._shift_x_int_to_turtle_screen(left),
            cls._shift_y_int_to_turtle_screen(top),
        )

    @classmethod
    def draw_circle(cls, color: str, center: tuple[int, int], radius: int):
        food = turtle.Turtle()
        food.penup()
        food.speed(0)
        food.setposition(
            cls._shift_x_int_to_turtle_screen(center[0]),
            cls._shift_y_int_to_turtle_screen(center[1]),
        )

        food.fillcolor(color)
        food.begin_fill()
        food.circle(radius)
        food.end_fill()

    @classmethod
    def update_clock(cls, fps: int) -> float:
        return 0.044

    @classmethod
    def get_screen_center(cls) -> tuple[int, int]:
        return int(cls.screen_width_px / 2), int(cls.screen_height_px / 2)

    @classmethod
    def get_players_move(cls) -> AllowedPlayerMoves:
        return cls.player_move

    @classmethod
    def _shift_x_int_to_turtle_screen(cls, number: int) -> int:
        return number - int(cls.screen_width_px / 2)

    @classmethod
    def _shift_y_int_to_turtle_screen(cls, number: int) -> int:
        return (number - int(cls.screen_height_px / 2)) * -1
