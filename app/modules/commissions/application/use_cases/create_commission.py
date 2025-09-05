from typing import Any, Dict
from bson import ObjectId

from app.modules.commissions.application.pipelines.steps import (
    GetBrokerDMNRulesStep,
    GetTransactionInvoiceStep,
)
from app.modules.commissions.domain.interfaces import (
    ITransactionRepository,
)
from app.modules.commissions.domain.interfaces import (
    IInvoiceRepository,
)
from app.modules.commissions.domain.interfaces import IPeriodStrategy
from app.shared.application.pipelines import AsyncPipeline
from app.shared.application.pipelines.steps import (
    SaveRawDataStep,
)
from app.shared.domain.interfaces import IRawRepository


class CreateCommissionUseCase:
    def __init__(
        self,
        raw_repository: IRawRepository,
        period_strategy: IPeriodStrategy,
        invoice_repository: IInvoiceRepository,
        transaction_repository: ITransactionRepository,
    ):
        self.raw_repository = raw_repository
        self.period_strategy = period_strategy
        self.invoice_repository = invoice_repository
        self.transaction_repository = transaction_repository

    async def execute(self, data: Dict[str, Any]) -> ObjectId:

        pipeline = AsyncPipeline(
            steps=[
                SaveRawDataStep(self.raw_repository),
                GetBrokerDMNRulesStep(),
                GetTransactionInvoiceStep(
                    self.invoice_repository, self.period_strategy
                ),
            ]
        )
        result = await pipeline.run(data)
        print(result)
        # return await self.transaction_repository.save(
        #    Transaction.create(CreateTransactionDTO(**result)).to_model()
        # )
