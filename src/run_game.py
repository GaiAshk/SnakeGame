from configuration.allowed_player_moves import AllowedPlayerMoves
from configuration.constants import SCREEN_HEIGHT_PX, SCREEN_WIDTH_PX, SCREEN_COLOR, FPS
from src.deps_wrappers.pygame_wrapper import Pygame
from src.shapes.snake import Snake
from src.shapes.food import Food
from typing import Optional

snake: Optional[Snake] = None
delta_time: float = 0.0


def draw_snake() -> None:
    print("draw snake")

    global snake
    if not snake:
        # draw first snake at screen center
        screen_center_x, screen_center_y = Pygame.get_screen_center()
        snake = Snake(screen_center_x, screen_center_y)
        Pygame.draw_rect(snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height)
        return None

    # update snake location
    player_move = get_player_move()
    snake.update_location(player_move, delta_time)
    Pygame.draw_rect(snake.color, snake.x_pos, snake.y_pos, snake.width, snake.height)


def get_player_move() -> AllowedPlayerMoves:
    return Pygame.get_players_move()


def create_food():
    print("create_food")
    pass


def update_clock():
    global delta_time
    delta_time = Pygame.tick_clock(FPS)


def run_game():

    Pygame.init()
    Pygame.set_screen_mode(SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX, SCREEN_COLOR)
    Pygame.init_clock()

    running = True

    while running:
        if Pygame.should_quit():
            running = False

        Pygame.wipe_screen()

        draw_snake()

        create_food()

        Pygame.flip()

        update_clock()

    Pygame.quit()
