"""App config module."""
import os
import logging
import sys


# LOG ----------------------------------------------------------
DEFAULT_LOGGER_NAME = 'CesarTest'
_LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)
_LOGGER.setLevel(logging.DEBUG)
_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

_h_console = logging.StreamHandler(sys.stdout)
_h_console.setLevel(logging.WARNING)
_h_console.setFormatter(_formatter)

if os.getenv('FLASK_ENV', 'development') == 'production':
    _h_file = logging.FileHandler(filename='/data/mose.log')
    _h_file.setLevel(logging.DEBUG)
    _h_file.setFormatter(_formatter)
    _LOGGER.addHandler(_h_file)
else:
    _h_console.setLevel(logging.DEBUG)

_LOGGER.addHandler(_h_console)
# ---------------------------------------------------------------


def get_logger():
    """Get logger by module name"""
    # TODO: Create log rules
    return logging.getLogger(DEFAULT_LOGGER_NAME)


class BaseConfig(object):  # pylint disable=useless-object-inheritance
    SECRET_KEY = os.environ['SECRET_KEY']
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    # Cache ----------------------------------------------------------
    CACHE_REDIS_HOST = os.environ['REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['REDIS_PORT']
    CACHE_REDIS_URL = f'redis://redis:{CACHE_REDIS_PORT}/0'
    CACHE_REDIS_DEFAULT_USER = os.environ['REDIS_DEFAULT_USER']
    CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24  # default is 24 hours
    CACHE_TYPE = os.environ['CACHE_TYPE']
    # ----------------------------------------------------------------
