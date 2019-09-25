from settings import LOGGER_NAME

# Set DEBUG True for developers/maintainers
DEBUG = False

FORMAT = ('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - '
          '%(lineno)d - %(message)s')
if DEBUG:
    LEVEL = 'DEBUG'
else:
    LEVEL = 'NOTSET'

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
            'level': LEVEL,
            'formatter': 'simpleFormatter',
            'class': 'logging.StreamHandler',
        },
        'fileHandler': {
            'level': LEVEL,
            'formatter': 'simpleFormatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '',
            'maxBytes': 1024,
            'backupCount': 5,
            'encoding': 'utf-8',
        }
    },
    'loggers': {
        LOGGER_NAME: {
            'handlers': ['streamHandler', 'fileHandler'],
            'level': LEVEL,
        }
    }
}
