from app.shared.application.pipelines.steps import AsyncStep
from typing import Dict, Any

from app.shared.domain.interfaces import IRawRepository


class SaveRawDataStep(AsyncStep):
    def __init__(self, raw_repository: IRawRepository):
        self.raw_repository = raw_repository

    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        raw = await self.raw_repository.save(data)
        data.update({"raw_transaction_id": str(raw)})
        return data
