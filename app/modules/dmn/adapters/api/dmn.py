from typing import Optional
from fastapi import APIRouter, Depends
from app.modules.dmn.adapters.dtos import CreateDMNDTO, GetDMNDTO
from app.modules.dmn.application.use_cases import CreateDMNUseCase, GetDMNUseCase
from app.modules.dmn.infrastructure.repositories import DMNRepository
from app.shared.infrastructure.mongodb import get_collection


dmn_routes = APIRouter(prefix="/dmn", tags=["dmn"])


async def create_dmn_use_case():
    collection = await get_collection("dmn_rules")
    return CreateDMNUseCase(repository=DMNRepository(collection))


@dmn_routes.post("", status_code=200, response_model=None)
async def create_dmn(
    data: CreateDMNDTO, use_case: CreateDMNUseCase = Depends(create_dmn_use_case)
) -> None:
    await use_case.execute(data)


async def get_dmn(
    broker_id: str,
) -> Optional[GetDMNDTO]:
    collection = await get_collection("dmn_rules")
    use_case = GetDMNUseCase(repository=DMNRepository(collection))
    return await use_case.execute(broker_id)
