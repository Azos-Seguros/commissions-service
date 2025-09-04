from typing import Any, Dict
from bson import ObjectId

from app.modules.commissions.application.pipelines.steps import GetBrokerDMNRulesStep
from app.modules.commissions.domain.interfaces import (
    ITransactionRepository,
)
from app.shared.application.pipelines import AsyncPipeline
from app.shared.application.pipelines.steps import (
    SaveRawDataStep,
)
from app.shared.domain.interfaces import IRawRepository


class CreateCommissionUseCase:
    def __init__(
        self,
        transaction_repository: ITransactionRepository,
        raw_repository: IRawRepository,
    ):
        self.transaction_repository = transaction_repository
        self.raw_repository = raw_repository

    async def execute(self, data: Dict[str, Any]) -> ObjectId:

        pipeline = AsyncPipeline(
            steps=[
                SaveRawDataStep(self.raw_repository),
                GetBrokerDMNRulesStep(),
            ]
        )
        result = await pipeline.run(data)
        print(result)
        # return await self.transaction_repository.save(
        #    Transaction.create(CreateTransactionDTO(**result)).to_model()
        # )
