from helpers.database import getConnection
from typing import List
from HeartRate.domain.repository import HeartRateRepository
from HeartRate.domain.model import HeartRateData


class MySQLHeartRateRepository(HeartRateRepository):
    def __init__(self):
        self.connection = getConnection()

    def get_all(self) -> List[HeartRateData]:
        if not self.connection:
            return []

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT measurement FROM HEART_RATES")
        rows = cursor.fetchall()

        heartRate_data_list = [HeartRateData(**row) for row in rows]
        cursor.close()

        return heartRate_data_list