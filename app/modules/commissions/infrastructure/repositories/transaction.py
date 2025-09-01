from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.commissions.domain.interfaces import ITransactionRepository
from app.modules.commissions.domain.models import TransactionModel
from app.shared.infrastructure.repositories import PostgresRepository


class TransactionRepository(ITransactionRepository, PostgresRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, TransactionModel)
