import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


DATABASE_URL = "sqlite+aiosqlite:///./sqlite.db"

engine = create_async_engine(DATABASE_URL, echo=True)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logging.error(f"Database session error: {e}")
            # Можна зробити rollback, якщо транзакція не закрилася
            await session.rollback() 
            raise