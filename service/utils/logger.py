import logging

SQLALCHEMY_ERROR_LOG_MSG = "An error occurred while working with SQLAlchemy: {}"
PANDAS_ERROR_LOG_MSG = "An error occurred while working with PandasDataFrame: {}"
JSON_ERROR = "Ошибка во время конвертации PandasDataFrame в json"


def init_logger():
    logging.basicConfig(
        level=logging.WARNING,
        filename="api_sber.log",
        format="%(asctime)s, %(levelname)s, %(message)s, %(name)s",
    )

    logger_init = logging.getLogger(__name__)
    logger_init.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger_init.addHandler(handler)
    return logger_init


api_logger = init_logger()
