from fastapi import APIRouter, Depends

from app.modules.dmn.adapters.dtos.dmn import CreateDMNDTO
from app.modules.dmn.application.use_cases import CreateDMNUseCase
from app.modules.dmn.infrastructure.repositories import DMNRepository
from app.shared.infrastructure.postgres import get_session

from sqlalchemy.ext.asyncio import AsyncSession

dmn_routes = APIRouter(prefix="/dmn", tags=["dmn"])


def create_dmn_use_case(session: AsyncSession = Depends(get_session)):
    return CreateDMNUseCase(repository=DMNRepository(session=session))


@dmn_routes.post("/", status_code=200, response_model=None)
async def create_dmn(
    data: CreateDMNDTO, use_case: CreateDMNUseCase = Depends(create_dmn_use_case)
) -> dict:
    await use_case.execute(data)
