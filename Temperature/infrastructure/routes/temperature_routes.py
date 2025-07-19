# routes/temperature_routes.py
from fastapi import APIRouter
from Temperature.infrastructure.MySQL import MySQLTemperatureRepository
from Temperature.application.usecase.statistic_useCase import TemperatureSummary
from Temperature.application.usecase.classify_measurement_useCase import GetClassifyUseCase

temperature_router = APIRouter()

@temperature_router.get("/temperatures/statistics")
def get_statistics():
    repo = MySQLTemperatureRepository()
    use_case = TemperatureSummary(repo)
    return use_case.execute()

@temperature_router.get("/temperatures/classify")
def get_classify():
    repo = MySQLTemperatureRepository()
    use_case = GetClassifyUseCase(repo)
    return use_case.execute()
