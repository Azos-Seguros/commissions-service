"""Singleton pattern implementations (abstract and concrete)."""

from abc import ABCMeta
from typing import Any, Dict


class ABCSingleton(ABCMeta):
    """Abstract singleton implementation to be used as metaclass."""

    _instances: Dict[type, "ABCSingleton"] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> "ABCSingleton":
        if cls not in cls._instances:
            cls._instances[cls] = super(ABCSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear_instances(cls) -> None:
        """Delete current instances."""
        if cls in cls._instances:
            del cls._instances[cls]

    def has_instance(cls) -> bool:
        """Check if Singleton class has a current instance."""
        return cls in cls._instances
