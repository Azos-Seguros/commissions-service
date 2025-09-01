"""
Configuração do MongoDB usando motor (async driver).
"""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.shared.settings import settings
from app.shared.utils.singleton import ABCSingleton


class MongoDB(metaclass=ABCSingleton):
    """Classe singleton para gerenciar conexão com MongoDB."""

    def __init__(self, mongodb_uri: str = settings.mongodb_uri) -> None:
        if not hasattr(self, "_client"):
            self._client: AsyncIOMotorClient = None
            self._database: AsyncIOMotorDatabase = None
            self._mongodb_uri = mongodb_uri

    async def connect(self) -> None:
        """Estabelece conexão com o MongoDB."""
        if self._client is None:
            # Extrai configurações da URI do MongoDB
            # mongodb://username:password@host:port/database
            self._client = AsyncIOMotorClient(self._mongodb_uri)
            self._database = self._client.get_database("commissions-service")

            # Testa a conexão
            await self._client.admin.command("ping")

    async def disconnect(self) -> None:
        """Fecha a conexão com o MongoDB."""
        if self._client:
            self._client.close()
            self._client = None
            self._database = None

    def get_database(self) -> AsyncIOMotorDatabase:
        """Retorna a instância do banco de dados."""
        if self._database is None:
            raise RuntimeError("MongoDB não está conectado. Chame connect() primeiro.")
        return self._database

    def get_collection(self, collection_name: str):
        """Retorna uma coleção específica."""
        return self.get_database()[collection_name]


# Instância singleton global
mongodb = MongoDB()


async def get_mongodb() -> MongoDB:
    """
    Dependency para injetar MongoDB.

    Returns:
        Instância do MongoDB
    """
    await mongodb.connect()
    return mongodb


async def get_collection(collection_name: str):
    """
    Dependency para injetar uma coleção específica.

    Args:
        collection_name: Nome da coleção

    Returns:
        Coleção do MongoDB
    """
    await mongodb.connect()
    return mongodb.get_collection(collection_name)
