from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Oxygen.infrastructure.routes.routes import oxygen_router
from HeartRate.infrastructure.routes.routes import heartRate_router
from Temperature.infrastructure.routes.temperature_routes import temperature_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite esos orígenes
    allow_credentials=True,
    allow_methods=["*"],     # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],     # Permite todos los headers
)
app.include_router(oxygen_router, prefix="/api/v1", tags=["oxygen"])
app.include_router(heartRate_router, prefix="/api/v1",tags=["heartRate"])
app.include_router(temperature_router, prefix="/api/v1", tags=["temperature"])

