from typing import Optional
from app.modules.dmn.domain.entities import DMN
from app.shared.domain.interfaces import IBaseRepository


class IDMNRepository(IBaseRepository[DMN]):
    """Interface para repositório de DMN."""

    async def get_by_broker_id(self, broker_id: str) -> Optional[DMN]:
        pass
