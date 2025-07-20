from Oxygen.domain.models import OxygenData
from typing import List
import pandas as pd


class StatisticService:
    def __init__(self, data: List[OxygenData]):
        self.data = data
        self.measurements = [d.measurement for d in data]

        if not data:
            self.df = pd.DataFrame()
        else:
            self.df = pd.DataFrame([{
                "measurement": d.measurement
            } for d in data])

    def mean(self):
        return self.df["measurement"].mean()

    def median(self):
        return self.df["measurement"].median()

    def mode(self):
        return self.df["measurement"].mode()[0]

    def get_dataframe(self):
        return self.df
