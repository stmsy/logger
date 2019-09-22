# Set DEBUG True for for developers/maintainers
DEBUG = True

FORMAT = '%(asctime)s - %(lineno)d - %(levelname)s - %(module)s - %(message)s'
if DEBUG:
    LEVEL = 10
else:
    LEVEL = 20

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
        '': {
            'handlers': ['streamHandler', 'fileHandler'],
            'level': LEVEL,
        }
    }
}
