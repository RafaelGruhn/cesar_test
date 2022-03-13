'''Init root project'''
# pylint: disable=import-error
from crypt import methods
import os
import json

from flask import Flask, request, render_template
from flask_caching import Cache
from flask_socketio import SocketIO, emit

from config import BaseConfig, get_logger
from morse.decrypt import decrypt_message
from morse.exceptions import MessageError


LOGGER = get_logger()


def create_app():
    '''
        Create and configure the app
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(BaseConfig)
    if app.config['FLASK_ENV'] == 'development':
        socketio = SocketIO(app, logger=True)
    else:
        socketio = SocketIO(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    cache = Cache(app)  # Initialize Cache

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/decrypt_morse', methods=['POST'])
    @cache.cached(timeout=app.config['CACHE_DEFAULT_TIMEOUT'], query_string=False)
    def decrypt_from_http():
        try:
            json_data = json.loads(request.data)
            message = json_data.get('message')
            if not message:
                raise MessageError('Key "message" not found in request data!')
            LOGGER.debug(f'Receive message to decrypt from POST. Message: {message}')

            # Convert morse message to currently text
            decrypted_message, message_arg, status_code = call_decrypt_message(message)

        except json.JSONDecodeError as error:
            LOGGER.error(f'Decode message error. Error: {error}')
            return 'Error: request data not in json format!', 400
        except MessageError as error:
            return error, 400
        except Exception as error:
            return 

    @socketio.on('decrypt_morse')
    def decrypt_from_socket(data):
        try:
            message = data.get('message')
            if not message:
                raise MessageError('Key "message" not found in request data!')
            LOGGER.debug(f'Receive message to decrypt from Socket. Message: {message}')

            # Convert morse message to currently text
            decrypted_message, message_arg, status_code = call_decrypt_message(message)
            emit('decrypted_morse', {
                'message': decrypted_message, "message_arg": message_arg, "code": status_code})

        except json.JSONDecodeError as error:
            LOGGER.error(f'Decode message error. Error: {error}')
        except MessageError as error:
            LOGGER.error(f'Decode message error. Error: {error}')
        except Exception as error:
            LOGGER.error(f'Decode message error. Error: {error}')

    @cache.memoize(timeout=app.config['CACHE_DEFAULT_TIMEOUT'])
    def call_decrypt_message(message: str):
        """Call function from morse module"""
        LOGGER.info('Calling function to decrypt message from socket or http')
        return decrypt_message(message)

    socketio.run(app)
    return app
