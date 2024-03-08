import random


def get_random_int(start: int, stop: int, step: int = 1) -> int:
    return random.randrange(start, stop, step)
