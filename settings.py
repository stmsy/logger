import logging
from pathlib import Path

from params import LOGGER_NAME

PWD = Path.cwd()
LOG_DIR = PWD.joinpath('logs')
CONFIG_DIR = PWD.joinpath('config')

LEVELS = {
    0: logging.NOTSET, 1: logging.DEBUG, 2: logging.INFO,
    3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL
}

TYPE_ERROR_MESSAGE = "both args must be integers"
