from abc import ABC, abstractmethod
from typing import List
from Temperature.domain.models import TemperatureData

class TemperatureRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[TemperatureData]:
        pass