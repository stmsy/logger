#!/usr/bin/env python

from pathlib import Path

PWD = Path.cwd()
LOG_DIR = PWD.joinpath('logs')
CONFIG_DIR = PWD.joinpath('config')

LOGGER_NAME = 'sampleLogger'

TYPE_ERROR_MESSAGE = "both arguments must be integers"
