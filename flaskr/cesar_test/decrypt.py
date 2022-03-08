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
    words = message.strip().split('message')
    decrypted_message = ''

    try:
        for word in words:
            decrypted_message.append(LEGEND[word])
    except KeyError:
        LOGGER.exception(f'Error while decrypting message. Invalid morcy string: {word}')
        return 

