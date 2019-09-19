#!/usr/bin/env python

from add import add
from mult import mult
from logger import logger
from sub import sub


if __name__ == '__main__':
    # Log messages with several levels
    logger.log(20, "info")
    logger.log(30, "warning")
    logger.log(50, "critical")
    logger.info("info")
    logger.warning("warning")
    logger.critical("critical")

    # Log messages from another module
    add(1, 2)
    sub(1, 2)
    mult(1.0, 2)
