from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.shared.settings import settings
from app.shared.adapters.api import core_routes
from app.modules.dmn.adapters.api import dmn_routes

app = FastAPI(
    title="Commissions Service",
    description="Commissions Service",
    version="0.1.0",
    docs_url="/docs",
    root_path=settings.root_path,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(core_routes)
app.include_router(dmn_routes)
