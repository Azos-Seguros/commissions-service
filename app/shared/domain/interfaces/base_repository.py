from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class IBaseRepository(ABC, Generic[T]):
    """Interface base para repositórios seguindo os princípios da Clean Architecture."""

    @abstractmethod
    async def save(self, entity: T) -> str:
        """
        Salva uma entidade no repositório.

        Args:
            entity: Entidade a ser salva

        Returns:
            Entidade salva com ID gerado
        """
        pass

    @abstractmethod
    async def get_by_id(self, entity_id: str) -> Optional[T]:
        """
        Busca uma entidade por ID.

        Args:
            entity_id: ID da entidade

        Returns:
            Entidade encontrada ou None
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[T]:
        """
        Busca todas as entidades.

        Returns:
            Lista de todas as entidades
        """
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        """
        Atualiza uma entidade existente.

        Args:
            entity: Entidade a ser atualizada

        Returns:
            Entidade atualizada
        """
        pass

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        """
        Remove uma entidade por ID.

        Args:
            entity_id: ID da entidade a ser removida

        Returns:
            True se removida com sucesso, False caso contrário
        """
        pass

    @abstractmethod
    async def exists(self, entity_id: str) -> bool:
        """
        Verifica se uma entidade existe.

        Args:
            entity_id: ID da entidade

        Returns:
            True se existe, False caso contrário
        """
        pass
