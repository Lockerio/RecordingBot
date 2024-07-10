from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import DATABASE_URL


async_engine = create_async_engine(DATABASE_URL)
session_maker = async_sessionmaker(async_engine, expire_on_commit=False)
Base = declarative_base()
