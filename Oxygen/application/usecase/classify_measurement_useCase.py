from Oxygen.application.service.classify_measurement_service import ClassifyMeasurementService
from typing import List, Dict
from collections import Counter
from Oxygen.domain.repository import OxygenRepository


class GetClassifyUseCase():
    def __init__(self,repo : OxygenRepository):
        self.repo = repo
        
    def execute(self,user_id: int) -> Dict[str, List]:
        data = self.repo.get_all(user_id)
        
        if not data:
            return {"mensaje": "No hay mediciones registradas para este usuario."}
        
        service = ClassifyMeasurementService(data)
        counts = Counter(service.classifications)
        
        return {
            "labels":["Excelente","Regular","Bajo","Muy bajo"],
            "values": [
                counts.get("Excelente", 0),
                counts.get("Regular", 0),
                counts.get("Bajo", 0),
                counts.get("Muy bajo",0)
            ]
        }