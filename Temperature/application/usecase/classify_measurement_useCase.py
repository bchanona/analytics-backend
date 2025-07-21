from Temperature.application.services.classify_measurement_service import ClassifyMeasurementService
from typing import List, Dict
from collections import Counter
from Temperature.domain.repository import TemperatureRepository


class GetClassifyUseCase():
    def __init__(self,repo : TemperatureRepository):
        self.repo = repo
        
    def execute(self, user_id : int) -> Dict[str, List]:
        data = self.repo.get_all(user_id)
        
        if not data:
            return {"mensaje": "No hay mediciones registradas para este usuario."}
        
        service = ClassifyMeasurementService(data)
        counts = Counter(service.classifications)
        
        return {
            "labels":["Excelente","Regular","Bajo","Alta"],
            "values": [
                counts.get("Excelente", 0),
                counts.get("Regular", 0),
                counts.get("Bajo", 0),
                counts.get("Alta",0)
            ]
        }
