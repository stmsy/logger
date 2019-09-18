#!/usr/bin/env python

FORMAT = '%(asctime)s:%(lineno)d:%(levelname)s:%(module)s:%(name)s:%(message)s'

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simpleFormatter': {
            'format': FORMAT
        }
    },
    'handlers': {
        'streamHandler': {
            'level': 'DEBUG',
            'formatter': 'simpleFormatter',
            'class': 'logging.StreamHandler',
        },
        'fileHandler': {
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '',
            'maxBytes': 1024,
            'backupCount': 5,
            'encoding': 'utf-8',
        }
    },
    'loggers': {
        '': {
            'handlers': ['streamHandler', 'fileHandler'],
            'level': "DEBUG",
        }
    }
}
