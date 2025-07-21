from helpers.database import getConnection
from typing import List
from HeartRate.domain.repository import HeartRateRepository
from HeartRate.domain.model import HeartRateData


class MySQLHeartRateRepository(HeartRateRepository):
    def __init__(self):
        self.connection = getConnection()

    def get_all(self,user_id : int) -> List[HeartRateData]:
        if not self.connection:
            return []

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT measurement FROM HEART_RATES WHERE user_id = %s",(user_id,))
        rows = cursor.fetchall()

        heartRate_data_list = [HeartRateData(**row) for row in rows]
        cursor.close()

        return heartRate_data_list