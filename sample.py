#!/usr/bin/env python

from datetime import date
import logging
from logging.config import dictConfig

from config.params import config
from settings import LOG_DIR, LOGGER_NAME
from utils import add


if __name__ == '__main__':
    # Create 'logs' directory if necessary
    if not LOG_DIR.exists():
        LOG_DIR.mkdir()

    # Create filepath for log output
    today = str(date.today())
    filepath = LOG_DIR.joinpath(f'{today}.log')
    config['handlers']['fileHandler']['filename'] = filepath

    # Set logger with specified config
    dictConfig(config)
    logger = logging.getLogger(LOGGER_NAME)

    # Log messages with several levels
    logger.log(20, "info")
    logger.log(30, "warning")
    logger.log(50, "critical")
    logger.info("info")
    logger.warning("warning")
    logger.critical("critical")

    # Log messages from another module
    add(1, 2)
    add(1.0, 2)
