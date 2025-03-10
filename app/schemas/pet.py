from pydantic import BaseModel
from datetime import date

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    birth_date: date
    owner_name: str
    chip_number: str

class PetResponse(PetCreate):
    id: int

    class Config:
        from_attributes = True