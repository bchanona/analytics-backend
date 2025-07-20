from HeartRate.application.service.classify_measurement_service import ClassifyMeasurementService
from typing import List, Dict
from collections import Counter
from HeartRate.domain.repository import HeartRateRepository


class GetClassifyUseCase():
    def __init__(self,repo : HeartRateRepository):
        self.repo = repo
        
    def execute(self) -> Dict[str, List]:
        data = self.repo.get_all()
        service = ClassifyMeasurementService(data)
        counts = Counter(service.classifications)
        
        return {
            "labels":["Excelente","Normal","Elevado","Taquicardia","Bradicardia"],
            "values": [
                counts.get("Excelente", 0),
                counts.get("Normal", 0),
                counts.get("Elevado", 0),
                counts.get("Taquicardia",0),
                counts.get("Bradicardia",0)
            ]
        }