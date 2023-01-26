from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class CustomTimedLoggerHandler(TimedRotatingFileHandler):
    def __init__(
        self, path, filename, when, interval, backupCount, *args, **kwargs
    ) -> None:

        f_name = filename.split(".")

        filename = f"{path}/{f_name[0]}{datetime.strftime(datetime.now(), '%Y-%m-%d')}.{f_name[1]}"

        super().__init__(
            filename, when, interval, backupCount, *args, **kwargs
        )
