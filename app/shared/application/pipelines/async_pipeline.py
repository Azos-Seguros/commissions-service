from typing import List, Dict, Any
import logging

from app.shared.domain.interfaces import IAsyncPipeline, IAsyncStep


logger = logging.getLogger(__name__)


class AsyncPipeline(IAsyncPipeline):
    def __init__(self, steps: List[IAsyncStep]) -> None:
        if not steps:
            raise ValueError("Pipeline deve ter pelo menos um step")

        self.steps = steps
        logger.info("AsyncPipeline inicializado", extra={"steps_count": len(steps)})

    async def run(self, data: Dict[str, Any]) -> Dict[str, Any]:

        logger.info("------------------------------------------------")
        logger.info("Iniciando execução do pipeline")
        logger.info("Dados de entrada: %s", data)
        current_data = data.copy()

        for i, step in enumerate(self.steps):
            try:
                logger.debug(
                    f"Executando step {i+1}/{len(self.steps)}",
                    extra={"step_type": type(step).__name__},
                )

                current_data = await step.run(current_data)

                logger.debug(
                    f"Step {i+1} concluído",
                    extra={
                        "step_type": type(step).__name__,
                        "output_keys": list(current_data.keys()),
                    },
                )

                logger.info("Dados após o step %s: %s", i + 1, current_data)

            except Exception as e:
                logger.error(
                    f"Erro no step {i+1}",
                    extra={
                        "step_type": type(step).__name__,
                        "error": str(e),
                        "step_index": i,
                    },
                )
                raise Exception(
                    f"Erro no step {i+1} ({type(step).__name__}): {str(e)}"
                ) from e

        logger.info("------------------------------------------------")
        logger.info(
            "Pipeline executado com sucesso",
            extra={"final_keys": list(current_data.keys())},
        )

        return current_data

    def add_step(self, step: IAsyncStep) -> None:
        self.steps.append(step)
        logger.info(
            "Step adicionado ao pipeline", extra={"step_type": type(step).__name__}
        )

    def get_steps_count(self) -> int:
        return len(self.steps)
