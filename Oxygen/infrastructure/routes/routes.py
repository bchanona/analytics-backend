from fastapi import APIRouter
from Oxygen.infrastructure.MySQL import MySQLOxygenRepository
from Oxygen.application.usecase.statistic_useCase import OxygenSummary
from Oxygen.application.usecase.classify_measurement_useCase import GetClassifyUseCase

oxygen_router = APIRouter()

@oxygen_router.get("/oxygen/statistics")
def getstatistics():
    repo =  MySQLOxygenRepository()
    use_case = OxygenSummary(repo)
    return use_case.execute()
        
@oxygen_router.get("/oxygen/classify")
def getclassify():
    repo = MySQLOxygenRepository()
    use_case = GetClassifyUseCase(repo)
    return use_case.execute()