import logging
import sys

from src.configuration.constants import ConfigType, ConfigKeys
from src.utils.config_manager import ConfigManager


class GameLogger:

    def __init__(self):
        self._logger = logging.getLogger(
            ConfigManager.get(ConfigType.LOGGING, ConfigKeys.LOG_NAME)
        )
        self._logger.setLevel(
            ConfigManager.get(ConfigType.LOGGING, ConfigKeys.LOG_LEVEL)
        )

        _handler = logging.StreamHandler(sys.stdout)
        _formatter = logging.Formatter(
            ConfigManager.get_raw(ConfigType.LOGGING, ConfigKeys.LOG_FMT),
            ConfigManager.get_raw(ConfigType.LOGGING, ConfigKeys.LOG_DATE_FMT),
        )
        _handler.setFormatter(_formatter)
        self._logger.addHandler(_handler)

    @property
    def get_logger(self) -> logging.Logger:
        return self._logger


game_logger = GameLogger()
logger: logging.Logger = game_logger.get_logger
