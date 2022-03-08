'''Init root project'''
import os

from flask import Flask
from flask import request
from flask_caching import Cache

from config import BaseConfig, get_logger
from cesar_test.decrypt import decrypt_message


LOGGER = get_logger()


def create_app():
    '''
        Create and configure the app
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(BaseConfig)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # cache = Cache(app)  # Initialize Cache

    @app.route('/decrypt_morse', methods=['POST', 'GET'])
    # @cache.cached(timeout=app.config['CACHE_DEFAULT_TIMEOUT'], query_string=False)
    def decrypt():
        print(request.data)
        LOGGER.info(f'Receive message to decrypt. Message: ')
        return 'Hello, World!'

    return app
