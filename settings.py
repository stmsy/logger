import logging
from pathlib import Path

from params import LOGGER_NAME

PWD = Path.cwd()
LOG_DIR = PWD.joinpath('logs')
CONFIG_DIR = PWD.joinpath('config')

LEVELS = {
    0: logging.NOTSET, 5: logging.DEBUG, 4: logging.INFO,
    3: logging.WARNING, 2: logging.ERROR, 1: logging.CRITICAL
}

TYPE_ERROR_MESSAGE = "both args must be integers"
