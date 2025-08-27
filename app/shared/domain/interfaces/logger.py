from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class ILogger(ABC):
    """Interface para o sistema de logging seguindo os princípios da Clean Architecture."""

    @abstractmethod
    def debug(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de debug."""
        pass

    @abstractmethod
    def info(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem informativa."""
        pass

    @abstractmethod
    def warning(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de aviso."""
        pass

    @abstractmethod
    def error(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de erro."""
        pass

    @abstractmethod
    def exception(
        self,
        message: str,
        exc_info: Optional[Exception] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Registra uma exceção com traceback."""
        pass
