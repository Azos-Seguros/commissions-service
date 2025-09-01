from fastapi import APIRouter, Depends
from app.modules.commissions.adapters.dtos import CreateTransactionDTO
from app.modules.commissions.application.use_cases import (
    CreateCommissionUseCase,
)
from app.modules.commissions.infrastructure.repositories import (
    TransactionRepository,
)
from app.shared.infrastructure.postgres import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.infrastructure.repositories import RawRepository
from app.shared.infrastructure.mongodb import get_collection


commission_routes = APIRouter(prefix="/commission", tags=["commission"])


async def create_transaction_use_case(session: AsyncSession = Depends(get_session)):
    raw_collection = await get_collection("raw_transactions")
    return CreateCommissionUseCase(
        transaction_repository=TransactionRepository(session=session),
        raw_repository=RawRepository(collection=raw_collection),
    )


@commission_routes.post("", status_code=200, response_model=None)
async def create_transaction(
    data: CreateTransactionDTO,
    use_case: CreateCommissionUseCase = Depends(create_transaction_use_case),
) -> None:
    await use_case.execute(data)
