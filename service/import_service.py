import os.path
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from typing import Tuple, Dict
from werkzeug.utils import secure_filename

from service.utils.responses import (
    EMPTY_FILE_PATH,
    ERROR_UPLOADING_FILE,
    FILE_NOT_FOUND,
    INCORRECT_FILE_TYPE,
    SUCCESS_FILE_UPLOADED,
)
from service.utils.queries import execute_query, TRUNCATE_AND_CREATE_TABLE
from service.utils.parsing import (
    allowed_file_type,
    data_processing,
    df_to_sql,
    PandasDataFrame,
)

from service.utils.logger import api_logger, SQLALCHEMY_ERROR_LOG_MSG, PANDAS_ERROR_LOG_MSG


class ImportService:
    @staticmethod
    def import_file_to_sql(file: Dict) -> Tuple[Dict[str, str], int]:
        if not file:
            return {"message": EMPTY_FILE_PATH}, 400
        file: str = file.get("path")
        file: str = secure_filename(file)
        if not allowed_file_type(file):
            return {"message": INCORRECT_FILE_TYPE}, 400
        if not os.path.exists(file):
            return {"message": FILE_NOT_FOUND.format(file)}, 400
        try:
            execute_query(TRUNCATE_AND_CREATE_TABLE)
        except SQLAlchemyError as e:
            api_logger.error(SQLALCHEMY_ERROR_LOG_MSG.format(e))
            return {"message": ERROR_UPLOADING_FILE.format(file)}, 500
        try:
            df: PandasDataFrame = data_processing(file)
        except pd.errors as e:
            api_logger.error(PANDAS_ERROR_LOG_MSG.format(e))
            return {"message": ERROR_UPLOADING_FILE.format(file)}, 500
        try:
            df_to_sql(df)
        except SQLAlchemyError as e:
            api_logger.error(SQLALCHEMY_ERROR_LOG_MSG.format(e))
            return {"message": ERROR_UPLOADING_FILE.format(file)}, 500
        return {"message": SUCCESS_FILE_UPLOADED.format(file)}, 201
