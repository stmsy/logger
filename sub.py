from logger import logger
from settings import LEVELS, TYPE_ERROR_MESSAGE
from utils import are_int


def sub(num1: int, num2: int, verbosity: int = 4) -> int:
    """Subtract one number from another if they both are integers."""
    level = LEVELS[verbosity]
    logger.setLevel(level)
    if are_int(num1, num2):
        return num1 - num2
    else:
        logger.error(TYPE_ERROR_MESSAGE)
        raise TypeError(TYPE_ERROR_MESSAGE)
