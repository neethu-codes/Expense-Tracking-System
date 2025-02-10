import logging

def set_up_logging(filename,log_file='server.log', level=logging.DEBUG):

    logger = logging.getLogger(filename)
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
# logger->file_handler->formatter