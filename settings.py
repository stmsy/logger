import logging
from pathlib import Path

PWD = Path.cwd()
LOG_DIR = PWD.joinpath('logs')
CONFIG_DIR = PWD.joinpath('config')

LEVELS = {
    0: logging.NOTSET, 1: logging.DEBUG, 2: logging.INFO,
    3: loggging.WARNING, 4: loggig.ERROR, 5: logging.CRITICAL
}

LOGGER_NAME = 'sampleLogger'

TYPE_ERROR_MESSAGE = "both args must be integers"
