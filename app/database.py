from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///.tasks.db"

engine = create_async_engine(DATABASE_URL,echo = True)

SessionLocal =  sessionmaker(
    engine, # type: ignore
    class_= AsyncSession,
    expire_on_commit=False
) # type: ignore

Base =  declarative_base()