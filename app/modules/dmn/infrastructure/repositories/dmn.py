from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.dmn.domain.models.dmn import DMNModel
from app.modules.dmn.domain.interfaces.dmn_repository import IDMNRepository
from app.shared.infrastructure.repositories import PostgresRepository


class DMNRepository(IDMNRepository, PostgresRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, DMNModel)
