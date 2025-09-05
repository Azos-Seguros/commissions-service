from datetime import datetime
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.commissions.domain.enums import InvoiceStatus, InvoiceType
from app.modules.commissions.domain.interfaces import IInvoiceRepository
from app.modules.commissions.domain.models import InvoiceModel
from app.shared.infrastructure.repositories import PostgresRepository


class InvoiceRepository(IInvoiceRepository, PostgresRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, InvoiceModel)

    async def get_current_invoice(
        self,
        beneficiary_id: str,
        invoice_status: InvoiceStatus,
        invoice_type: InvoiceType,
        start_date: datetime,
        end_date: datetime,
    ) -> Optional[InvoiceModel]:
        query = select(InvoiceModel).where(
            InvoiceModel.beneficiary_id == beneficiary_id,
            InvoiceModel.status == invoice_status,
            InvoiceModel.invoice_type == invoice_type,
            InvoiceModel.created_at >= start_date,
            InvoiceModel.created_at <= end_date,
        )
        result = await self.session.execute(query)
        return result.scalars().first()
