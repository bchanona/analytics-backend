from helpers.database import getConnection
from typing import List
from Oxygen.domain.repository import OxygenRepository
from Oxygen.domain.models import OxygenData


class MySQLOxygenRepository(OxygenRepository):
    def __init__(self):
        self.connection = getConnection()

    def get_all(self) -> List[OxygenData]:
        if not self.connection:
            return []

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT measurement FROM OXYGENS")
        rows = cursor.fetchall()

        oxygen_data_list = [OxygenData(**row) for row in rows]
        cursor.close()

        return oxygen_data_list
