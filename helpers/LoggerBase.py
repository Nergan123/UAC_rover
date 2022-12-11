import logging


class LoggingHandler:
    """ Class for logg handling """
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
