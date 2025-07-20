from pydantic import BaseModel


class TemperatureData(BaseModel):
    measurement: float
