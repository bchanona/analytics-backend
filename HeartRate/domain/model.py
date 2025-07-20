from pydantic import BaseModel

class HeartRateData(BaseModel):
    measurement: float