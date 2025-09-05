from typing import Type, Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.domain.interfaces.base_repository import IBaseRepository, T


class PostgresRepository(IBaseRepository[T]):
    def __init__(self, session: AsyncSession, entity_class: Type[T]):
        self.session = session
        self.entity_class = entity_class

    async def get_by_id(self, entity_id: str) -> Optional[T]:
        return await self.session.get(self.entity_class, entity_id)

    async def get_all(self) -> List[T]:
        result = await self.session.execute(select(self.entity_class))
        return result.scalars().all()

    async def save(self, entity: T) -> str:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity.id

    async def update(self, entity: T) -> T:
        await self.session.merge(entity)
        await self.session.commit()
        return entity

    async def delete(self, entity_id: str) -> bool:
        obj = await self.session.get(self.entity_class, entity_id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
            return True
        return False

    async def exists(self, entity_id: str) -> bool:
        obj = await self.session.get(self.entity_class, entity_id)
        return obj is not None
