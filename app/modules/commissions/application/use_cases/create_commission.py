from bson import ObjectId

from app.modules.commissions.adapters.dtos import CreateTransactionDTO
from app.modules.commissions.domain.interfaces import (
    ITransactionRepository,
)
from app.shared.domain.interfaces import IRawRepository


class CreateCommissionUseCase:
    def __init__(
        self,
        transaction_repository: ITransactionRepository,
        raw_repository: IRawRepository,
    ):
        self.transaction_repository = transaction_repository
        self.raw_repository = raw_repository

    async def execute(self, data: CreateTransactionDTO) -> ObjectId:
        raw = await self.raw_repository.save(data)
        print(raw)
        # return await self.transaction_repository.save(
        #    Transaction.create(data, raw.id).to_model()
        # )
