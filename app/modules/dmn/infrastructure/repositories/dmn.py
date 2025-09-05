from typing import Optional
from app.modules.dmn.domain.entities import DMN
from app.modules.dmn.domain.interfaces import IDMNRepository
from app.shared.infrastructure.repositories import MongoRepository


class DMNRepository(IDMNRepository, MongoRepository):
    def __init__(self, collection):
        super().__init__(collection, DMN)

    async def get_by_broker_id(self, broker_id: str) -> Optional[DMN]:
        result = await self.collection.find_one({"broker_id": broker_id})
        return DMN(**result) if result else None
