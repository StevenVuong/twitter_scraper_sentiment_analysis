import logging

formatting = "%(levelname)s: " \
             "%(asctime)s -> " \
             "%(name)s - " \
             "line %(lineno)d: " \
             "%(message)s"


def add_stream_handler(logger: logging.Logger):
    formatter = logging.Formatter(formatting)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    