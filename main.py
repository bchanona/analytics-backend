from fastapi import FastAPI
from Temperature.infrastructure.routes.temperature_routes import temperature_router


app = FastAPI()

app.include_router(temperature_router, prefix="/api/v1", tags=["temperature"])
