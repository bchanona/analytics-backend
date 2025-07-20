from Temperature.domain.models import TemperatureData
from typing import List

class ClassifyMeasurementService:
    def __init__(self, data: List[TemperatureData]):
        self.data = data
        self.measurements = [d.measurement for d in data]
        self.classifications = self.classify_all()

    def classify(self, value: float) -> str:
        if 36.5 <= value <= 37.5:
            return 'Excelente'
        elif 35.5 <= value < 36.5:
            return 'Regular'
        elif 0 <= value > 35.5:
            return 'Bajo'
        else:
            return 'Alta'

    def classify_all(self) -> List[str]:
        return [self.classify(value) for value in self.measurements]

  