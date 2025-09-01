from typing import Any
from app.shared.domain.interfaces import IRawRepository
from app.shared.infrastructure.repositories import MongoRepository


class RawRepository(IRawRepository, MongoRepository):
    def __init__(self, collection):
        super().__init__(collection, Any)
