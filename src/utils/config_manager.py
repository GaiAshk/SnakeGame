import configparser
from src.configuration.constants import CONFIG_FILE_PATH


class ConfigManager:

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)

    @classmethod
    def get(cls, config_type: str, config_key: str) -> str:
        return cls.config[config_type][config_key]

    @classmethod
    def get_int(cls, config_type: str, config_key: str) -> int:
        return int(cls.config[config_type][config_key])
