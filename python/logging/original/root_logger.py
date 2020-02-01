
"""https://realpython.com/python-logging/"""

import logging

"""5 Types of levels:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
"""

def intro():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

"""Can configure the logger with:

basicConfig(**kwargs)
level: The root logger will be set to specified severity level
filename: Specifies the filename
filemode: If filename is given, open in this mode. Default is a
format: Formar of the log message
"""

def level():
    # Note this needs to be called at the very top
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This will get logged now')

def filelog():
    # root - WARNING - This will get logged to a file
    logging.basicConfig(level=logging.DEBUG, filename='app.log',
                        format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')    


"""Formatting the Output"""
def option1():
    # 388-WARNING-This is a Warning
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    logging.warning('This is a Warning')

def option2():
    # 2019-04-20 17:58:52,907 - Admin logged in
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Admin logged in')

def option3():
    # 20-Apr-19 17:59:38 - Admin logged out
    logging.basicConfig(format='%(asctime)s - %(message)s', 
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('Admin logged out')


"""Logging Variable Data"""
name = 'John'

logging.error('%s original string error', name)
logging.error(f'{name} fstring error')

"""Stack Traces"""
a = 5
b = 0
try:
    c = a/b
except Exception as e:
    logging.error(".error -> Exception occurred", exc_info=True)
    logging.exception(".exception --> Exception occured")


def test_name():
    print(__name__)


