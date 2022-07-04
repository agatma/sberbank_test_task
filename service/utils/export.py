import json
from typing import TypeVar, Dict, Union, List

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")
SQLAlchemyEngine = TypeVar("sqlalchemy.engine.cursor.LegacyCursorResult")
DeltaJson = Dict[str, Union[int, str, float]]


def df_to_json(df: PandasDataFrame) -> List[DeltaJson]:
    df = df.to_dict(orient="records")
    df = json.dumps(df, default=str)
    json_df = json.loads(df)
    return json_df


def sql_to_json(row: SQLAlchemyEngine, delta_lag=False) -> DeltaJson:
    data = {"id": row.id, "rep_dt": str(row.rep_dt), "delta": row.delta}
    if delta_lag:
        data["delta_lag"] = row.delta_lag
    return data
