from sqlalchemy.orm import Session
from app.db.models.pet import Pet
from app.schemas.pet import PetCreate

class PetRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_pet(self, pet_data: PetCreate) -> Pet:
        pet = Pet(**pet_data.dict())
        self.db.add(pet)
        self.db.commit()
        self.db.refresh(pet)
        return pet
