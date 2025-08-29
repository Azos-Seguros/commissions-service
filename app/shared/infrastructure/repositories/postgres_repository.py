from typing import Type, Optional, List
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.domain.interfaces.base_repository import IBaseRepository, T


class PostgresRepository(IBaseRepository[T]):
    def __init__(self, session: AsyncSession, entity_class: Type[T]):
        self.session = session
        self.entity_class = entity_class

    async def get_by_id(self, entity_id: str) -> Optional[T]:
        return await self.session.get(self.entity_class, entity_id)

    async def get_all(self) -> List[T]:
        result = await self.session.execute(self.session.query(self.entity_class))
        return result.scalars().all()

    async def save(self, entity: T) -> None:
        await self.session.execute(insert(self.entity_class), entity.__dict__)
        await self.session.commit()

    async def delete(self, entity_id: str) -> None:
        obj = await self.session.get(self.entity_class, entity_id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
