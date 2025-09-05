from typing import Type, Optional, List
from bson import ObjectId
from app.shared.domain.interfaces.base_repository import IBaseRepository, T
from app.shared.utils import to_dict


class MongoRepository(IBaseRepository[T]):
    def __init__(self, collection, entity_class: Type[T]):
        self.collection = collection
        self.entity_class = entity_class

    async def get_by_id(self, entity_id: str) -> Optional[T]:
        result = await self.collection.find_one({"_id": ObjectId(entity_id)})
        return self.entity_class(**result) if result else None

    async def get_all(self) -> List[T]:
        cursor = self.collection.find()
        return [self.entity_class(**doc) async for doc in cursor]

    async def save(self, entity: T) -> str:
        result = await self.collection.insert_one(to_dict(entity))
        return str(result.inserted_id)

    async def update(self, entity: T) -> T:
        await self.collection.update_one(
            {"_id": ObjectId(entity.id)}, {"$set": to_dict(entity)}
        )
        return entity

    async def delete(self, entity_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(entity_id)})
        return result.deleted_count > 0

    async def exists(self, entity_id: str) -> bool:
        count = await self.collection.count_documents({"_id": ObjectId(entity_id)})
        return count > 0
