from Oxygen.domain.models import OxygenData
from abc import ABC, abstractmethod
from typing import List

class OxygenRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[OxygenData]:
        pass    