import logging
import sys
from typing import Optional

from src.configuration.constants import ConfigType, ConfigKeys
from src.utils.config_manager import ConfigManager


class Logger:
    
    def __init__(self):
        self._logger: logging.Logger = Optional[None]

    def init_logger(self):
        self._logger = logging.getLogger(ConfigManager.get(ConfigType.LOGGING, ConfigKeys.LOG_NAME))
        self._logger.setLevel(ConfigManager.get(ConfigType.LOGGING, ConfigKeys.LOG_LEVEL))

        _handler = logging.StreamHandler(sys.stdout)
        _formatter = logging.Formatter(
                ConfigManager.get_raw(ConfigType.LOGGING, ConfigKeys.LOG_FMT),
                ConfigManager.get_raw(ConfigType.LOGGING, ConfigKeys.LOG_DATE_FMT),
        )
        _handler.setFormatter(_formatter)
        self._logger.addHandler(_handler)

    @property
    def get_logger(self):
        return self._logger


logger = Logger()
logger.init_logger()
logger = logger.get_logger
