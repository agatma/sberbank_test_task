import pathlib

from db import db
from models import DeltaModel
from pandas import pandas as pd
from export import PandasDataFrame


def allowed_file_type(filename: str) -> bool:
    allowed_extensions = set([".xlsx", ".xls"])
    extension = pathlib.Path(filename).suffix
    return extension in allowed_extensions


def data_processing(file: str) -> PandasDataFrame:
    df: PandasDataFrame = pd.read_excel(
        file, header=0, dtype={"Delta": str}, parse_dates=["Rep_dt"]
    )
    df = df.sort_values(by=["Rep_dt"])
    df["Delta"] = df["Delta"].str.replace(",", ".")
    df["Delta"] = df["Delta"].astype("float64")
    return df


def df_to_sql(df: PandasDataFrame) -> None:
    # Прохожу циклом по df и добавляю в сессию - чтобы была одна транзакция (комлю объекты)
    for row in df.itertuples():
        file = DeltaModel(row[1], row[2])
        file.save()
    # Делаем коммит для всех объектов сразу (тратим меньше времени)
    db.session.commit()
