from fastapi import FastAPI
from HeartRate.infrastructure.routes.routes import heartRate_router

app = FastAPI()

app.include_router(heartRate_router, prefix="/api/v1",tags=["heartRate"])