from sqlalchemy import Table, MetaData
from sqlalchemy.sql import text
from sqlalchemy_views import CreateView
from service.utils.queries import SELECT_DATA_FOR_VIEW


view = Table("delta_view", MetaData())
definition = text(SELECT_DATA_FOR_VIEW)

delta_view = CreateView(view, definition, or_replace=True)
