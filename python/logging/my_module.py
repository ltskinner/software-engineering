
import logging
logger = logging.getLogger()  # if no __name__, gets root logger


def funct_with_logger():
    logger.info("logging from submodule to logger defined in main")
