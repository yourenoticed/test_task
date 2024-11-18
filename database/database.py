from sqlalchemy import Table, Column, Integer, String, Text, Date, Boolean, CHAR, Engine, MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    "sqlite+aiosqlite:///./database/db.db", echo=True)
session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
