from pydantic import BaseModel

class SensorMeta(BaseModel):
    name: str
    property_prefix: str