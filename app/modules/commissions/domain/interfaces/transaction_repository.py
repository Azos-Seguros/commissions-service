from app.modules.commissions.domain.entities import Transaction
from app.shared.domain.interfaces.base_repository import IBaseRepository


class ITransactionRepository(IBaseRepository[Transaction]):
    """Interface para repositório de Transaction."""

    pass
