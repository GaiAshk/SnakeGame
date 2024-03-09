CONFIG_FILE_PATH = "src/configuration/config.ini"


class ConfigType:
    GAME = "game"
    SCREEN = "screen"
    LOGGING = "logging"


class ConfigKeys:
    # game configs
    FPS = "FPS"
    GAME_LIB = "GAME_LIB"
    DRAWING_LIB = "DRAWING_LIB"
    SNAKE_COLOR = "SNAKE_COLOR"
    SNAKE_WIDTH_PX = "SNAKE_WIDTH_PX"
    SNAKE_HEIGHT_PX = "SNAKE_HEIGHT_PX"
    FOOD_COLOR = "FOOD_COLOR"
    FOOD_RADIUS = "FOOD_RADIUS"
    FOOD_EATING_SENSITIVITY = "FOOD_EATING_SENSITIVITY"
    KEY_MOVEMENT_PX = "KEY_MOVEMENT_PX"
    BORDER_PX_Y = "BORDER_PX_Y"
    BORDER_PX_X = "BORDER_PX_X"

    # screen configs
    SCREEN_WIDTH_PX = "SCREEN_WIDTH_PX"
    SCREEN_HEIGHT_PX = "SCREEN_HEIGHT_PX"
    SCREEN_COLOR = "SCREEN_COLOR"

    # log configs
    LOG_NAME = "LOG_NAME"
    LOG_LEVEL = "LOG_LEVEL"
    LOG_FMT = "LOG_FMT"
    LOG_DATE_FMT = "LOG_DATE_FMT"
