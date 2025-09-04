from typing import Dict, Any
import logging

from app.shared.domain.interfaces import IAsyncStep

logger = logging.getLogger(__name__)


class AsyncStep(IAsyncStep):
    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]: ...
