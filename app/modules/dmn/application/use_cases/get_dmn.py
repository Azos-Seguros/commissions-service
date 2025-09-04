from typing import Optional
from app.modules.dmn.adapters.dtos import GetDMNResponseDTO
from app.modules.dmn.domain.interfaces import IDMNRepository


class GetDMNUseCase:
    def __init__(self, repository: IDMNRepository):
        self.repository = repository

    async def execute(self, broker_id: str) -> Optional[GetDMNResponseDTO]:
        dmn = await self.repository.get_by_broker_id(broker_id)
        return dmn.to_dto() if dmn else None
