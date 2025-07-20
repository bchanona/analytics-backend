from Temperature.application.services.statistics_service import StatisticService
from Temperature.domain.repository import TemperatureRepository
import numpy as np

class TemperatureSummary:
    def __init__(self, repo: TemperatureRepository):
        self.repo = repo
    
    def execute(self):
        data = self.repo.get_all()
        stats = StatisticService(data)
        
        return {
            "Media: ":np.round(stats.mean(),4),
            "Mediana: ": np.round(stats.median(),4),
            "Moda: ": np.round(stats.mode(),4)   
        }