from pydantic import BaseModel
from datetime import date

class VaccineCreate(BaseModel):
    pet_id: int
    vaccine_date: date
    vaccine_name: str

class VaccineResponse(VaccineCreate):
    id: int

    class Config:
        from_attributes = True