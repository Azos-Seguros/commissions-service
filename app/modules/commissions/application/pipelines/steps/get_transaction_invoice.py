from datetime import datetime
from typing import Any, Dict
from app.modules.commissions.adapters.dtos import CreateInvoiceDTO
from app.modules.commissions.domain.entities import Invoice
from app.modules.commissions.domain.enums import InvoiceStatus, InvoiceType
from app.modules.commissions.domain.interfaces import (
    IInvoiceRepository,
    IPeriodStrategy,
)
from app.modules.dmn.domain.enums import RecurrenceType
from app.shared.application.pipelines.steps import AsyncStep


class GetTransactionInvoiceStep(AsyncStep):
    def __init__(
        self, invoice_repository: IInvoiceRepository, period_strategy: IPeriodStrategy
    ):
        self.invoice_repository = invoice_repository
        self.period_strategy = period_strategy
        self.invoice_id: str | None = None

    def get_invoice_period(
        self, created_at: datetime, recurrence: RecurrenceType, cutoff_day: int | None
    ):
        strategy = self.period_strategy.get_strategy(recurrence)
        return strategy.get_period(
            created_at=created_at,
            cutoff_day=cutoff_day,
        )

    async def create_invoice(self, dmn: Dict[str, Any], end_date: datetime):
        invoice = Invoice.create(
            CreateInvoiceDTO(
                net_amount=0.0,
                gross_amount=0.0,
                payment_date=end_date,
                status=InvoiceStatus.OPEN,
                invoice_type=InvoiceType.COMMISSION.value,
                beneficiary_id=dmn["broker_id"],
            )
        )
        await self.invoice_repository.save(invoice.to_model())
        self.invoice_id = invoice.id

    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        dmn = data["dmn"]

        start_date, end_date = self.get_invoice_period(
            created_at=datetime.now(),
            cutoff_day=dmn["cutoff_day"],
            recurrence=dmn["recurrence_type"],
        )

        current_invoice = await self.invoice_repository.get_current_invoice(
            invoice_status=InvoiceStatus.OPEN,
            beneficiary_id=dmn["broker_id"],
            invoice_type=InvoiceType.COMMISSION,
            start_date=start_date,
            end_date=end_date,
        )

        if current_invoice:
            self.invoice_id = current_invoice.id
        else:
            await self.create_invoice(dmn, end_date)

        data.update({"invoice_id": self.invoice_id})
        return data
