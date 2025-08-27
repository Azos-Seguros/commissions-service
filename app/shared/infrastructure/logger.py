import logging
import sys
from typing import Any, Dict, Optional

from app.shared.domain.interfaces.logger import ILogger


class Logger(ILogger):
    """Implementação concreta do logger usando a biblioteca logging padrão do Python."""

    def __init__(self, name: str, level: int = logging.INFO):
        """
        Inicializa o logger.

        Args:
            name: Nome do logger
            level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        # Evita duplicação de handlers
        if not self._logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self) -> None:
        """Configura os handlers do logger."""
        # Handler para console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        # Formato do log
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)

        self._logger.addHandler(console_handler)

    def _log_with_extra(
        self, level: int, message: str, extra: Optional[Dict[str, Any]] = None
    ) -> None:
        """Método auxiliar para logging com dados extras."""
        if extra:
            self._logger.log(level, f"{message} | Extra: {extra}")
        else:
            self._logger.log(level, message)

    def debug(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de debug."""
        self._log_with_extra(logging.DEBUG, message, extra)

    def info(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem informativa."""
        self._log_with_extra(logging.INFO, message, extra)

    def warning(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de aviso."""
        self._log_with_extra(logging.WARNING, message, extra)

    def error(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Registra uma mensagem de erro."""
        self._log_with_extra(logging.ERROR, message, extra)

    def exception(
        self,
        message: str,
        exc_info: Optional[Exception] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Registra uma exceção com traceback."""
        if extra:
            self._logger.exception(f"{message} | Extra: {extra}", exc_info=exc_info)
        else:
            self._logger.exception(message, exc_info=exc_info)
