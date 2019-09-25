from datetime import date
from logging import Logger

from config.params import config, DEBUG
from settings import LEVELS, LOG_DIR

# Create 'logs' directory if necessary
if not LOG_DIR.exists():
    LOG_DIR.mkdir()

# Create filepath for log output
today = str(date.today())
filepath = LOG_DIR.joinpath(f'{today}.log')
config['handlers']['fileHandler']['filename'] = filepath


def is_verbosity_valid(verbosity: int) -> bool:
    """Check whether verbosity is set properly."""
    if verbosity not in (0, 1, 2, 3, 4, 5):
        return False
    if DEBUG:
        if verbosity == 0:
            return False
    return True


def set_level(verbosity: int, logger: Logger) -> None:
    """Set the specified log lelvel if valid."""
    if is_verbosity_valid(verbosity):
        level = LEVELS[verbosity]
        logger.setLevel(level)
    else:
        raise ValueError("verbosity must be set properly")
