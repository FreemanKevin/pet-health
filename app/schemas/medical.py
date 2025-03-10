from pydantic import BaseModel
from datetime import date

class MedicalCreate(BaseModel):
    pet_id: int
    visit_date: date
    description: str

class MedicalResponse(MedicalCreate):
    id: int

    class Config:
        from_attributes = True