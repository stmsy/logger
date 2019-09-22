from logger import logger


def _is_int(num: int) -> bool:
    """Check whether the number is integer."""
    return isinstance(num, int)


def are_int(num1: int, num2: int) -> bool:
    """Check whether the numbers are both integers."""
    if _is_int(num1) and _is_int(num2):
        logger.debug("both args are integer")
        return True
    else:
        logger.debug("at least one of args is not integer")
        return False
