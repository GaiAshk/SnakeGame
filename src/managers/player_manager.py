from src.modles.modles import AllowedPlayerMoves
from src.deps_wrappers.pygame_wrapper import Pygame


class PlayerManager:

    @staticmethod
    def get_player_move() -> AllowedPlayerMoves:
        return Pygame.get_players_move()
