from fastapi import FastAPI
from Oxygen.infrastructure.routes.routes import oxygen_router

app = FastAPI()

app.include_router(oxygen_router, prefix="/api/v1", tags=["oxygen"])