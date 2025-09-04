from abc import ABC, abstractmethod
from typing import Dict, Any

from app.shared.domain.interfaces import IAsyncStep


class IAsyncPipeline(ABC):
    @abstractmethod
    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa o pipeline com os dados fornecidos.

        Args:
            data: Dicionário contendo os dados de entrada.

        Returns:
            Dicionário contendo o resultado final após processamento por todos os steps.

        Raises:
            ValueError: Se os dados de entrada forem inválidos.
            Exception: Se qualquer step falhar durante a execução.
        """
        pass

    @abstractmethod
    def add_step(self, step: IAsyncStep) -> None:
        """
        Adiciona um novo step ao final do pipeline.

        Args:
            step: Step que implementa a interface AsyncStep.
        """
        pass

    @abstractmethod
    def get_steps_count(self) -> int:
        """
        Retorna o número de steps no pipeline.

        Returns:
            Número de steps no pipeline.
        """
        pass
