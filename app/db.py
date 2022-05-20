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

DATABASE_URL='mysql://root:@localhost/api-jwt'

db_engine = create_engine(DATABASE_URL)
metadata = MetaData()

Product = Table(
    'product',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('barcode', String),
    Column('name', String),
    Column('price', Integer),
    Column('is_active', TINYINT),
    Column('created_at', DateTime, default=func.NOW()),
    Column('modified_at', DateTime, default=func.NOW(), onupdate=func.NOW())   
)
database = Database(DATABASE_URL)