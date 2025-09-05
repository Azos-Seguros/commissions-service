from datetime import datetime
from typing import Optional
from app.modules.commissions.domain.enums import InvoiceType
from app.modules.commissions.domain.enums.invoice_status import InvoiceStatus
from app.modules.commissions.domain.models.invoice import InvoiceModel
from app.shared.domain.interfaces.base_repository import IBaseRepository


class IInvoiceRepository(IBaseRepository[InvoiceModel]):
    """Interface para repositório de Transaction."""

    async def get_current_invoice(
        self,
        beneficiary_id: str,
        invoice_status: InvoiceStatus,
        invoice_type: InvoiceType,
        start_date: datetime,
        end_date: datetime,
    ) -> Optional[InvoiceModel]:
        pass
