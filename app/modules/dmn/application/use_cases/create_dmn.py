from app.modules.dmn.domain.entities.dmn import DMN
from app.modules.dmn.infrastructure.repositories import DMNRepository
from app.modules.dmn.adapters.dtos import CreateDMNDTO


class CreateDMNUseCase:
    def __init__(self, repository: DMNRepository):
        self.repository = repository

    async def execute(self, data: CreateDMNDTO) -> DMN:
        return await self.repository.save(DMN.create(data).to_model())
