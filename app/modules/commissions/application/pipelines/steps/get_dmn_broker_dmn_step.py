from app.modules.dmn.adapters.api import get_dmn
from app.shared.application.pipelines.steps import AsyncStep
from typing import Dict, Any


class GetBrokerDMNRulesStep(AsyncStep):

    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        dmn = await get_dmn(data["broker_id"])
        data.update({"dmn": dmn})
        return data
