import logging
from typing import Optional

from app.shared.domain.interfaces import ILogger
from app.shared.infrastructure.logger import Logger
from app.shared.settings import settings


class LoggerService:
    """Serviço de logger na camada de infraestrutura seguindo os princípios da Clean Architecture."""

    _loggers: dict[str, ILogger] = {}

    @classmethod
    def create_logger(cls, name: str, level: Optional[str] = None) -> ILogger:
        """
        Cria ou retorna um logger existente.

        Args:
            name: Nome do logger
            level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)

        Returns:
            Instância do logger
        """
        if name in cls._loggers:
            return cls._loggers[name]

        # Determina o nível de log
        log_level = cls._get_log_level(level)

        # Cria nova instância
        logger = Logger(name, log_level)
        cls._loggers[name] = logger

        return logger

    @classmethod
    def get_logger(cls, name: str) -> ILogger:
        """
        Retorna um logger existente ou cria um novo.

        Args:
            name: Nome do logger

        Returns:
            Instância do logger
        """
        return cls.create_logger(name)

    @classmethod
    def _get_log_level(cls, level: Optional[str] = None) -> int:
        """
        Determina o nível de log baseado no parâmetro ou nas configurações do projeto.

        Args:
            level: Nível de log especificado

        Returns:
            Nível de log como inteiro
        """
        # Prioridade: parâmetro > configurações do projeto > padrão
        log_level = level or settings.log_level.upper()

        level_mapping = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
        }

        return level_mapping.get(log_level, logging.INFO)

    @classmethod
    def clear_loggers(cls) -> None:
        """Limpa o cache de loggers (útil para testes)."""
        cls._loggers.clear()


# Função de conveniência para obter logger rapidamente
def get_logger(name: str) -> ILogger:
    """
    Função de conveniência para obter um logger.

    Args:
        name: Nome do logger

    Returns:
        Instância do logger
    """
    return LoggerService.get_logger(name)
