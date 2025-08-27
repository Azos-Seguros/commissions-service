from typing import Type, Optional, List
from bson import ObjectId
from app.shared.domain.interfaces.base_repository import IBaseRepository, T


class MongoRepository(IBaseRepository[T]):
    def __init__(self, collection, entity_class: Type[T]):
        self.collection = collection
        self.entity_class = entity_class

    def get_by_id(self, entity_id: str) -> Optional[T]:
        data = self.collection.find_one({"_id": ObjectId(entity_id)})
        return self.entity_class(**data) if data else None

    def get_all(self) -> List[T]:
        return [self.entity_class(**doc) for doc in self.collection.find()]

    def save(self, entity: T) -> None:
        self.collection.update_one(
            {"_id": ObjectId(entity.id)}, {"$set": entity.dict()}, upsert=True
        )

    def delete(self, entity_id: str) -> None:
        self.collection.delete_one({"_id": ObjectId(entity_id)})
