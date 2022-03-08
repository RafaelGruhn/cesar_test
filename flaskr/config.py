"""App config module."""
import os
import logging
import sys


# LOG ----------------------------------------------------------
DEFAULT_LOGGER_NAME = 'CesarTest'
_LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)
_LOGGER.setLevel(logging.DEBUG)
_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
_h_file = logging.FileHandler(filename='/data/cesar_test.log')
_h_file.setLevel(logging.DEBUG)
_h_file.setFormatter(_formatter)

_h_console = logging.StreamHandler(sys.stdout)
_h_console.setLevel(logging.WARNING)
_h_console.setFormatter(_formatter)

_LOGGER.addHandler(_h_console)
_LOGGER.addHandler(_h_file)
# ---------------------------------------------------------------


def get_logger():
    """Get logger by module name"""
    # TODO: Create log rules
    return logging.getLogger(DEFAULT_LOGGER_NAME)


class BaseConfig(object):
    SECRET_KEY='dev'
    # Cache ----------------------------------------------------------
    CACHE_REDIS_HOST = os.environ['REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['REDIS_PORT']
    CACHE_REDIS_URL = f'redis://redis:{CACHE_REDIS_PORT}/0' 
    CACHE_REDIS_DEFAULT_USER = os.environ['REDIS_DEFAULT_USER']
    CACHE_DEFAULT_TIMEOUT = os.environ['DEFAULT_TIMEOUT']
    CACHE_TYPE = os.environ['CACHE_TYPE']
    # ----------------------------------------------------------------
