from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    func,
    DateTime,
    create_engine
)
from sqlalchemy.dialects.mysql import TINYINT

from databases import Database

DATABASE_URL = 'mysql://root:@localhost/api-jwt'

db_engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)
