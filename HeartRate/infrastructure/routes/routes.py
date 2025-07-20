from fastapi import APIRouter

from HeartRate.infrastructure.MySQL import MySQLHeartRateRepository
from HeartRate.application.usecase.statistics_useCase import HeartRateSummary
from HeartRate.application.usecase.classify_measurement_useCase import GetClassifyUseCase

heartRate_router = APIRouter()

@heartRate_router.get("/heartRate/statistics")
def getstatistics():
    repo = MySQLHeartRateRepository()
    usecase = HeartRateSummary(repo)
    return usecase.execute()

@heartRate_router.get("/heartRate/classify")
def getclassify():
    repo = MySQLHeartRateRepository()
    usecase = GetClassifyUseCase(repo)
    return usecase.execute()
    