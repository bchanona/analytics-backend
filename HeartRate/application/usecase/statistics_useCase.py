from HeartRate.application.service.statistics_service import StatisticService

from HeartRate.domain.repository import HeartRateRepository
import numpy as np

class HeartRateSummary:
    def __init__(self, repo: HeartRateRepository):
        self.repo = repo
    
    def execute(self):
        data = self.repo.get_all()
        stats = StatisticService(data)
        
        return {
            "Media: ":np.round(stats.mean(),4),
            "Mediana: ": np.round(stats.median(),4),
            "Moda: ": np.round(stats.mode(),4)   
        }