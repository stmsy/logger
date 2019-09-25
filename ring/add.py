from logging import getLogger
from logging.config import dictConfig

from logger import config, set_level
from settings import LOGGER_NAME, LEVELS, TYPE_ERROR_MESSAGE
from .utils import are_int

dictConfig(config)
logger = getLogger(LOGGER_NAME)


def add(num1: int, num2: int, verbosity: int = 4) -> int:
    """Add two numbers if they both are integers."""
    set_level(verbosity, logger)
    if are_int(num1, num2, logger):
        return num1 + num2
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
