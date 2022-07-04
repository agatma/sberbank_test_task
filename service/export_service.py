import json
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from typing import Tuple, Dict, Union

from db import db
from utils.logger import (
    api_logger,
    SQLALCHEMY_ERROR_LOG_MSG,
    PANDAS_ERROR_LOG_MSG,
    JSON_ERROR,
)
from utils.export import sql_to_json, df_to_json
from utils.parsing import PandasDataFrame
from utils.queries import (
    execute_query_and_return,
    SELECT_DATA_WITH_DELTA_LAG,
    SELECT_ALL_FROM_DELTA_MODEL,
)
from utils.responses import EXPORT_FILE_ERROR, ERROR_EXPORTING_FILE


class ExportService:
    @staticmethod
    def export_df(
        property: str, lag_num: int
    ) -> Tuple[Dict[str, Union[str, Dict]], int]:
        if property not in ("sql", "pandas"):
            return {"message": EXPORT_FILE_ERROR}, 400
        elif property == "sql":
            try:
                data = execute_query_and_return(
                    SELECT_DATA_WITH_DELTA_LAG, {"lag_num": lag_num}
                )
                df = [sql_to_json(row, delta_lag=True) for row in data]
            except SQLAlchemyError as e:
                api_logger.error(SQLALCHEMY_ERROR_LOG_MSG.format(e))
                return {"message": ERROR_EXPORTING_FILE}, 500
        else:
            try:
                df: PandasDataFrame = pd.read_sql_query(
                    SELECT_ALL_FROM_DELTA_MODEL, db.engine
                )
                df["delta_lag"] = df["delta"].shift(-lag_num)
            except pd.errors as e:
                api_logger.error(PANDAS_ERROR_LOG_MSG.format(e))
                return {"message": ERROR_EXPORTING_FILE}, 500
            try:
                df = df_to_json(df)
            except json.decoder.JSONDecodeError as e:
                api_logger.error(JSON_ERROR.format(e))
                return {"message": ERROR_EXPORTING_FILE}, 500
            except TypeError as e:
                api_logger.error(JSON_ERROR.format(e))
                return {"message": ERROR_EXPORTING_FILE}, 500
        return {"df": df}, 200
