from helpers.database import getConnection
from typing import List
from Temperature.domain.repository import TemperatureRepository
from Temperature.domain.models import TemperatureData

class MySQLTemperatureRepository(TemperatureRepository):
    def __init__(self):
        self.connection = getConnection()
    
    def get_all(self) -> List[TemperatureData]:
        if not self.connection:
            return []
        
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT measurement FROM TEMPERATURES")
        rows = cursor.fetchall()
        
        temperature_data_list = [TemperatureData(**row) for row in rows]
        
        cursor.close()
        return temperature_data_list
