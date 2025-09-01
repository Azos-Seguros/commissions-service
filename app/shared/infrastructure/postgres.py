from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.shared.settings import settings
from app.shared.utils.singleton import ABCSingleton


class Database(metaclass=ABCSingleton):
    _engine: Optional[AsyncEngine] = None
    _async_session: Optional[async_sessionmaker[AsyncSession]] = None

    Base = declarative_base()

    def __init__(self, db_uri: str = settings.postgres_uri) -> None:
        if self._engine is None:
            self._engine = create_async_engine(
                db_uri,
                pool_size=20,
                max_overflow=30,
                pool_pre_ping=True,
                pool_recycle=3600,
                pool_timeout=30,
            )
            self._async_session = async_sessionmaker(
                self._engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        if self._async_session is None:
            raise RuntimeError("Database not initialized")
        async with self._async_session() as session:
            try:
                yield session
            finally:
                await session.close()

    async def init_db(self) -> None:
        if self._engine is None:
            raise RuntimeError("Database not initialized")
        async with self._engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)

    async def close_db(self) -> None:
        if self._engine is None:
            raise RuntimeError("Database not initialized")
        await self._engine.dispose()

    async def check_connection(self) -> bool:
        if self._engine is None:
            raise RuntimeError("Database not initialized")
        try:
            async with self._engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
                return True
        except Exception:
            return False


db = Database()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.get_session() as session:
        yield session


async def init_db() -> None:
    await db.init_db()


async def close_db() -> None:
    await db.close_db()


async def check_db_connection() -> bool:
    return await db.check_connection()
