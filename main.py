from fastapi import FastAPI
from Oxygen.infrastructure.routes.routes import oxygen_router
from HeartRate.infrastructure.routes.routes import heartRate_router
from Temperature.infrastructure.routes.temperature_routes import temperature_router

app = FastAPI()

app.include_router(oxygen_router, prefix="/api/v1", tags=["oxygen"])
app.include_router(heartRate_router, prefix="/api/v1",tags=["heartRate"])
app.include_router(temperature_router, prefix="/api/v1", tags=["temperature"])

