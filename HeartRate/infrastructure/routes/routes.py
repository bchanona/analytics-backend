from fastapi import APIRouter

from HeartRate.infrastructure.MySQL import MySQLHeartRateRepository
from HeartRate.application.usecase.statistics_useCase import HeartRateSummary
from HeartRate.application.usecase.classify_measurement_useCase import GetClassifyUseCase

heartRate_router = APIRouter()

@heartRate_router.get("/heartRate/statistics/{user_id}")
def getstatistics(user_id : int):
    repo = MySQLHeartRateRepository()
    usecase = HeartRateSummary(repo)
    return usecase.execute(user_id)

@heartRate_router.get("/heartRate/classify/{user_id}")
def getclassify(user_id: int):
    repo = MySQLHeartRateRepository()
    usecase = GetClassifyUseCase(repo)
    return usecase.execute(user_id)
    