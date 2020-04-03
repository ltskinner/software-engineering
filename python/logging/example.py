

import my_module

if __name__ == '__main__':
    import logging
    import logging.config

    logging.config.fileConfig(fname="./logging.conf")

    my_module.funct_with_logger()
