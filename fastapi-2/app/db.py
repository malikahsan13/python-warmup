from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+aiomysql://root:password@localhsot:3306/mydb"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

async_session = sessionmaker(
    bind= engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()