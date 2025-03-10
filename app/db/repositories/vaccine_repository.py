from sqlalchemy.orm import Session
from app.db.models.vaccine import Vaccine
from app.schemas.vaccine import VaccineCreate

class VaccineRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_vaccine_record(self, vaccine_data: VaccineCreate) -> Vaccine:
        vaccine_record = Vaccine(**vaccine_data.dict())
        self.db.add(vaccine_record)
        self.db.commit()
        self.db.refresh(vaccine_record)
        return vaccine_record
