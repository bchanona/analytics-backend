from Oxygen.application.service.statistic_service import StatisticService

from Oxygen.domain.repository import OxygenRepository
import numpy as np

class OxygenSummary:
    def __init__(self, repo: OxygenRepository):
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