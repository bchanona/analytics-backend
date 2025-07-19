from Oxygen.domain.models import OxygenData
from typing import List

class ClassifyMeasurementService:
    def __init__(self, data: List[OxygenData]):
        self.data = data
        self.measurements = [d.measurement for d in data]
        self.classifications = self.classify_all()

    def classify(self, value: float) -> str:
        if 95 <= value <= 100:
            return 'Excelente'
        elif 91 <= value < 95:
            return 'Regular'
        elif 86 <= value < 91:
            return 'Bajo'
        elif 0 <= value < 86:
            return 'Muy bajo'

    def classify_all(self) -> List[str]:
        return [self.classify(value) for value in self.measurements]
