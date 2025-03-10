from fastapi import APIRouter, Depends
from app.schemas.medical import MedicalCreate, MedicalResponse
from app.db.repositories.medical_repository import MedicalRepository
from app.dependencies.database import get_db

router = APIRouter(prefix="/medical", tags=["medical"])

@router.post("/", response_model=MedicalResponse)
async def create_medical_record(
    medical_data: MedicalCreate,
    repo: MedicalRepository = Depends(get_db)
):
    return await repo.create_medical_record(medical_data)