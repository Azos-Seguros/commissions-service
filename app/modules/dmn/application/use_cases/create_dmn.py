from app.modules.dmn.domain.entities.dmn import DMN
from app.modules.dmn.domain.interfaces import IDMNRepository
from app.modules.dmn.adapters.dtos import CreateDMNDTO
from bson import ObjectId


class CreateDMNUseCase:
    def __init__(self, repository: IDMNRepository):
        self.repository = repository

    async def execute(self, data: CreateDMNDTO) -> ObjectId:
        return await self.repository.save(DMN.create(data))
