from pydantic import BaseSettings, ValidationError as PydanticValidationError
from loggers.logger import Logger
from functools import lru_cache
from utils.decorators import return_check

log = Logger()


class Env(BaseSettings):
    """
    Class to load the environment variable from the env file.
    """

    env_name: str = "local"
    host: str = "127.0.0.1"
    port: int = 8000
    db_name: str

    class Config:
        env_file = "../.env"


@return_check
@lru_cache
def get_settings() -> Env:
    """
    Get the environment from the loaded environments.

    Returns:
        Env: The instance of the environment class.
    """
    try:
        print("########### Getting all the environments ##############")
        env = Env()
    except PydanticValidationError as e:
        log = Logger.get_logger("exception")
        log.error(e.json())
        raise
    return env
