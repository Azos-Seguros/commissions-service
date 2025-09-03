from abc import ABC, abstractmethod
from typing import Dict, Any, Protocol


class IAsyncStep(ABC, Protocol):
    @abstractmethod
    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
