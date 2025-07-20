from pydantic import BaseModel

class OxygenData(BaseModel):
    measurement: float