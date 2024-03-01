CONFIG_FILE_PATH = "src/configuration/config.ini"


class ConfigType:
    GAME = "game"
    SCREEN = "screen"
    LOGGING = "logging"


class ConfigKeys:
    # game configs
    FPS = "FPS"
    SNAKE_COLOR = "SNAKE_COLOR"
    SNAKE_WIDTH_PX = "SNAKE_WIDTH_PX"
    SNAKE_HEIGHT_PX = "SNAKE_HEIGHT_PX"
    FOOD_COLOR = "FOOD_COLOR"
    KEY_MOVEMENT_PX = "KEY_MOVEMENT_PX"

    # screen configs
    SCREEN_WIDTH_PX = "SCREEN_WIDTH_PX"
    SCREEN_HEIGHT_PX = "SCREEN_HEIGHT_PX"
    SCREEN_COLOR = "SCREEN_COLOR"

    # log configs
    LOG_NAME = "LOG_NAME"
    LOG_LEVEL = "LOG_LEVEL"
    LOG_FMT = "LOG_FMT"
    LOG_DATE_FMT = "LOG_DATE_FMT"
