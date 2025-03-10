from sqlalchemy.orm import Session
from app.db.models.medical import Medical
from app.schemas.medical import MedicalCreate

class MedicalRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_medical_record(self, medical_data: MedicalCreate) -> Medical:
        medical_record = Medical(**medical_data.dict())
        self.db.add(medical_record)
        self.db.commit()
        self.db.refresh(medical_record)
        return medical_record
