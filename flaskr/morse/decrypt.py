'''Decrypt file'''
from config import get_logger


LOGGER = get_logger()

LEGEND = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '10'
}


def decrypt_message(message: str):
    '''
        Function that receives an encoded message and returns the decoded message.
        e. g.: "--- .." = "OI"
    '''
    words = message.split(' ')
    decrypted_message = ''

    try:
        for word in words:
            if word == '':
                decrypted_message = decrypted_message + ' '
            else:
                decrypted_message = decrypted_message + LEGEND[word]
    except KeyError:
        LOGGER.warning(f'Error while decrypting message. Invalid morse string: {word}')
        return decrypted_message, f'Error in part of Morse text. "{word}" as not recognized as valid Morse code!', 400
    except Exception as error:  # pylint: disable=broad-except
        LOGGER.exception(f'Error while decrypting message. Error: {error}')
        return decrypted_message, 'Internal Server Error', 500
    return decrypted_message, 'Success!', 200
