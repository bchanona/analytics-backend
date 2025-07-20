from fastapi import FastAPI

from Oxygen.infrastructure.routes.routes import oxygen_router
from HeartRate.infrastructure.routes.routes import heartRate_router

app = FastAPI()

app.include_router(oxygen_router, prefix="/api/v1", tags=["oxygen"])
app.include_router(heartRate_router, prefix="/api/v1",tags=["heartRate"])
