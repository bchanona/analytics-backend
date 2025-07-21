from fastapi import APIRouter
from Oxygen.infrastructure.MySQL import MySQLOxygenRepository
from Oxygen.application.usecase.statistic_useCase import OxygenSummary
from Oxygen.application.usecase.classify_measurement_useCase import GetClassifyUseCase

oxygen_router = APIRouter()

@oxygen_router.get("/oxygen/statistics/{user_id}")
def getstatistics(user_id: int):
    repo =  MySQLOxygenRepository()
    use_case = OxygenSummary(repo)
    return use_case.execute(user_id)
        
@oxygen_router.get("/oxygen/classify/{user_id}")
def getclassify(user_id: int):
    repo = MySQLOxygenRepository()
    use_case = GetClassifyUseCase(repo)
    return use_case.execute(user_id)