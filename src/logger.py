import logging
import datetime
import settings
from typing import List


def create_logger(formatter: logging.Formatter, handlers: List[logging.Handler]):
    logger = logging.getLogger("Gemini-logger")
    logger.setLevel(logging.INFO)

    for handler in handlers:
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


class FileHandler(logging.FileHandler):

    def __init__(self):
        settings.LOGS_DIR.mkdir(exist_ok=True)
        log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        super().__init__(settings.LOGS_DIR/log_filename, encoding="utf-8")


class ConsoleHandler(logging.StreamHandler):
    pass




formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = FileHandler()
console_handler = ConsoleHandler()

logger = create_logger(formatter, [file_handler, console_handler])