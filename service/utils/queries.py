from db import db
from sqlalchemy import text
from service.utils.export import SQLAlchemyEngine

TRUNCATE_AND_CREATE_TABLE = """
TRUNCATE delta_model RESTART IDENTITY;
CREATE TABLE if not exists delta_model (
    id serial4 NOT NULL, 
    rep_dt date NULL, 
    delta float8 NULL, 
    CONSTRAINT delta_model_pkey PRIMARY KEY (id)
);
"""

SELECT_ALL_FROM_DELTA_MODEL = "SELECT * FROM delta_model"

SELECT_DATA_FOR_VIEW = f"""SELECT  *, LAG(delta, 2) 
    OVER(ORDER BY to_char(rep_dt, 'YYYY-MM') DESC) AS delta_lag 
    FROM delta_model ORDER BY rep_dt;"""

SELECT_DATA_WITH_DELTA_LAG = f"""SELECT  *, LAG(delta, :lag_num) 
    OVER(ORDER BY to_char(rep_dt, 'YYYY-MM') DESC) AS delta_lag 
    FROM delta_view ORDER BY rep_dt;"""


def execute_query(query: str) -> None:
    db.engine.execute(text(query).execution_options(autocommit=True))


def execute_query_and_return(query: str, value) -> SQLAlchemyEngine:
    return db.engine.execute(text(query).execution_options(autocommit=True), value)
