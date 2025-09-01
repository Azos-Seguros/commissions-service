from app.modules.dmn.domain.entities.dmn import DMN
from app.modules.dmn.domain.interfaces import IDMNRepository
from app.shared.infrastructure.repositories import MongoRepository


class DMNRepository(IDMNRepository, MongoRepository):
    def __init__(self, collection):
        super().__init__(collection, DMN)
