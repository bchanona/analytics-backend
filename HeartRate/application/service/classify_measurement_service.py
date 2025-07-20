from HeartRate.domain.model import HeartRateData
from typing import List


class ClassifyMeasurementService:
    def __init__(self, data: List[HeartRateData]):
        self.data = data
        self.measurements = [d.measurement for d in data]
        self.classifications = self.classify_all()

    def classify(self, value: float) -> str:
        if 60 <= value <= 80:
            return 'Excelente'
        elif 81 <= value <= 90:
            return 'Normal'
        elif 91 <= value <= 100:
            return 'Elevado'
        elif value > 100:
            return 'Taquicardia'
        elif value < 60:
            return 'Bradicardia'

    def classify_all(self) -> List[str]:
        return [self.classify(value) for value in self.measurements]
