"""
SQLAlchemy model for connections to db_a
"""

from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, String, Boolean, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TableOne(Base):
    """
    description of what this table is for
    """

    __tablename__ = 'table_one'
    __table_args__ = ({"schema": "public"})

    uid = Column(UUID, primary_key=True,
                 server_default=text("uuid_generate_v4()"))
    col_a = Column(String, nullable=False)
    table_two_uid = Column(UUID, ForeignKey('public.table_two.uid'))
    de_datetime = Column(DateTime, server_default=func.now())

class TableTwo(Base):
    """
    description of what this table is for
    """

    __tablename__ = 'table_two'
    __table_args__ = ({"schema": "public"})

    uid = Column(UUID, primary_key=True,
                 server_default=text("uuid_generate_v4()"))
    value_boolean = Column(Boolean)
    de_datetime = Column(DateTime, server_default=func.now())
