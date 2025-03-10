from fastapi import APIRouter, Depends, UploadFile
from app.schemas.pet import PetCreate, PetResponse
from app.db.repositories.pet_repository import PetRepository
from app.dependencies.database import get_db
from app.storage.minio_client import get_minio_client

router = APIRouter(prefix="/pets", tags=["pets"])

@router.post("/", response_model=PetResponse)
async def create_pet(
    pet_data: PetCreate,
    repo: PetRepository = Depends(get_db)
):
    return await repo.create_pet(pet_data)

@router.post("/{pet_id}/avatar")
async def upload_avatar(
    pet_id: int,
    file: UploadFile,
    storage=Depends(get_minio_client)
):
    # 上传到MinIO的逻辑
    file_url = await storage.upload_file(
        bucket="pet-health",
        object_name=f"avatars/{pet_id}",
        file_data=file.file
    )
    return {"url": file_url}