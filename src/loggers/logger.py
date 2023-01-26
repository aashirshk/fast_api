import os
from logging.config import fileConfig
from logging import getLogger


class Logger:
    @staticmethod
    def get_logger(qualname="root"):

        path = os.path.join(os.path.dirname(__file__), "logger.ini")

        fileConfig(path)

        return getLogger(qualname)
