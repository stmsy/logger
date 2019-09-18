#!/usr/bin/env python

from datetime import date
import logging
from logging.config import dictConfig

from config.params import config
from settings import CONFIG_DIR, LOG_DIR


if __name__ == '__main__':
    # Create 'logs' directory if necessary
    if not LOG_DIR.exists():
        LOG_DIR.mkdir()

    # Create filepath for log output
    today = str(date.today())
    filepath = str(LOG_DIR.joinpath(f'{today}.log'))
    config['handlers']['fileHandler']['filename'] = filepath

    # Set logger with specified config
    dictConfig(config)
    logger = logging.getLogger('sample_logger')

    # Log messages with several levels
    logger.log(20, "info")
    logger.log(30, "warning")
    logger.log(100, "test")
    logger.info("info")
    logger.warning("warning")
