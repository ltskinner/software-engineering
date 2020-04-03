
import logging

"""Classes and functions

Instead of using:
    logger.log()
you should create your own object of the Logger class

Logger: Class whose objects will be used in the application code 
    directly to call the functions

LogRecord: Loggers automatically create LogRecord objects that have all
    the information related to the event being logged, like the name of
    the logger, the function, the line number, the message and more

Handler: Handlers send the LogRecord to the required output destination,
    like the console or a file. Handler is a base for subclasses like
    StreamHandler, FileHandler, SMTPHandler, HTTPHandler and more. These
    subclasses send the logging outputs to corresponding destinations, 
    like sys.stdout or a disk file

Formatter: This is where you specify the format of the output by
    specifying a string format that lists out the attributes that the
    output should contain
"""

def new_logger():
    logging.basicConfig(format='%(name)s - %(message)s')
    logger_name = 'example_logger'
    logger = logging.getLogger(logger_name)
    logger.warning('This is a warning')

"""
from root_logger import test_name
test_name()
print(__name__)
"""

"""Handlers"""

def custom():
    # Create custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler() # Goes to console I reckon
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')


def configged():
    import logging
    import logging.config

    logging.config.fileConfig(fname='log_file.conf', 
                              disable_existing_loggers=False)
    
    # Get the logger specified in the file
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')


