from HeartRate.domain.model import HeartRateData
from typing import List
from abc import ABC, abstractmethod

class HeartRateRepository(ABC):
    @abstractmethod
    def get_all(self)->List[HeartRateData]:
        pass