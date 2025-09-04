from typing import Dict, Any, Protocol


class IAsyncStep(Protocol):
    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
