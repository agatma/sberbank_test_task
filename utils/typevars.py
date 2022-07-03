from typing import TypeVar, Dict, Union

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")
SQLAlchemyEngine = TypeVar("sqlalchemy.engine.cursor.LegacyCursorResult")
DeltaJson = Dict[str, Union[int, str, float]]
