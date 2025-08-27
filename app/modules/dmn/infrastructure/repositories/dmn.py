from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from app.modules.dmn.domain.entities.dmn import DMN
from app.modules.dmn.domain.models.dmn import DMNModel
from app.modules.dmn.domain.interfaces.dmn_repository import IDMNRepository
from app.shared.infrastructure.repositories import PostgresRepository


class DMNRepository(IDMNRepository, PostgresRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, DMNModel)

    async def save(self, entity: DMNModel) -> None:
        """Salva a entidade convertendo para modelo primeiro."""
        await self.session.execute(insert(DMNModel), entity.__dict__)
        await self.session.commit()

    async def get_by_id(self, entity_id: str) -> Optional[DMN]:
        """Busca por ID e converte modelo para entidade."""
        model = await self.session.get(DMNModel, entity_id)
        if model:
            return self._model_to_entity(model)
        return DMN(**model)
