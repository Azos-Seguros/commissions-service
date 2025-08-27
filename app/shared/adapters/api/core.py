from fastapi import APIRouter, HTTPException

from app.shared.infrastructure.postgres import check_db_connection

core_routes = APIRouter(tags=["core"])


@core_routes.get("/healthcheck")
async def healthcheck() -> dict:
    """
    Verifica a saúde da aplicação, incluindo a conexão com o banco de dados.

    Returns:
        dict: Status da aplicação e do banco de dados
    """
    db_status = await check_db_connection()
    if not db_status:
        raise HTTPException(status_code=503, detail="Database connection failed")
    return {"status": "OK", "database": "connected"}
