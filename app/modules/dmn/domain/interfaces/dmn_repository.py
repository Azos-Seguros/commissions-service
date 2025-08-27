from app.modules.dmn.domain.entities.dmn import DMN
from app.shared.domain.interfaces.base_repository import IBaseRepository


class IDMNRepository(IBaseRepository[DMN]):
    pass
