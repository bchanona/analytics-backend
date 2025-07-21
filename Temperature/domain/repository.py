from abc import ABC, abstractmethod
from typing import List
from Temperature.domain.models import TemperatureData

class TemperatureRepository(ABC):
    @abstractmethod
    def get_all(self,user_id : int) -> List[TemperatureData]:
        pass