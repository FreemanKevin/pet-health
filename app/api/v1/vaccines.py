from fastapi import APIRouter, Depends
from app.schemas.vaccine import VaccineCreate, VaccineResponse
from app.db.repositories.vaccine_repository import VaccineRepository
from app.dependencies.database import get_db

router = APIRouter(prefix="/vaccines", tags=["vaccines"])

@router.post("/", response_model=VaccineResponse)
async def create_vaccine_record(
    vaccine_data: VaccineCreate,
    repo: VaccineRepository = Depends(get_db)
):
    return await repo.create_vaccine_record(vaccine_data)