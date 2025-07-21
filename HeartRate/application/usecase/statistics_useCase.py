from HeartRate.application.service.statistics_service import StatisticService

from HeartRate.domain.repository import HeartRateRepository
import numpy as np

class HeartRateSummary:
    def __init__(self, repo: HeartRateRepository):
        self.repo = repo
    
    def execute(self, user_id: int):
        data = self.repo.get_all(user_id)
        
        if not data:
            return {"mensaje": "No hay mediciones registradas para este usuario."}
        stats = StatisticService(data)
        
        return {
            "Media: ":np.round(stats.mean(),4),
            "Mediana: ": np.round(stats.median(),4),
            "Moda: ": np.round(stats.mode(),4)   
        }