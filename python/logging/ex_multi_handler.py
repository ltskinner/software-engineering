

"""
Add Python logging to a script that will
- log errors to STDERR
- info statements to STDOUT
- all levels to a file


https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
"""



import logging
import sys



logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')



stderr_handler = logging.StreamHandler(stream=sys.stderr)
stderr_handler.setLevel(logging.ERROR)
stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

file_handler = logging.FileHandler(filename='all_levels.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




logger.debug('debug level - sterr N, stdout N, file Y')
logger.info('info level - sterr N, stdout Y, file Y')
logger.error('error level - stderr Y, stdout Y, fileY')



# remember to close the handlers
for handler in logger.handlers:
    handler.close()
    logger.removeFilter(handler)

