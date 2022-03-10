'''Init root project'''
# pylint: disable=import-error
from crypt import methods
import os
import json

from flask import Flask, request, render_template
from flask_caching import Cache

from config import BaseConfig, get_logger
from cesar_test.decrypt import decrypt_message
from cesar_test.exceptions import MessageError


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

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')


    @app.route('/decrypt_morse', methods=['POST'])
    # @cache.cached(timeout=app.config['CACHE_DEFAULT_TIMEOUT'], query_string=False)
    def decrypt():
        try:
            json_data = json.loads(request.data)
            message = json_data.get('message')
            if not message:
                raise MessageError('Key "message" not found in request data!')
            LOGGER.info(f'Receive message to decrypt. Message: {message}')

            # Convert morse message to currently text
            decrypted_message, message_arg, status_code = decrypt_message(message)

        except json.JSONDecodeError as error:
            LOGGER.error(f'Decode message error. Error: {error}')
            return 'Error: request data not in json format!', 400
        except MessageError as error:
            return error, 400
        except Exception as error:
            return 

    return app
