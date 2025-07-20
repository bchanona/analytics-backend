from Oxygen.application.service.statistic_service import StatisticService

from Oxygen.domain.repository import OxygenRepository
import numpy as np

class OxygenSummary:
    def __init__(self, repo: OxygenRepository):
        self.repo = repo
    
    def execute(self):
        data = self.repo.get_all()
        stats = StatisticService(data)
        
        return {
            "Media: ":np.round(stats.mean(),4),
            "Mediana: ": np.round(stats.median(),4),
            "Moda: ": np.round(stats.mode(),4)   
        }