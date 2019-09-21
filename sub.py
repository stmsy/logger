from logger import logger
from settings import TYPE_ERROR_MESSAGE
from utils import are_int


def sub(num1: int, num2: int) -> int:
    """Subtract one number from another if they both are integers."""
    if are_int(num1, num2):
        return num1 - num2
    else:
        logger.error(TYPE_ERROR_MESSAGE)
        raise TypeError(TYPE_ERROR_MESSAGE)
