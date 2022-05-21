from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
    func,
    DateTime,
)
from sqlalchemy.dialects.mysql import TINYINT

from app.models import metadata


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
