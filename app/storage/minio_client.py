from minio import Minio
from app.core.config import settings

class MinioClient:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE
        )
    
    async def upload_file(self, bucket: str, object_name: str, file_data):
        if not self.client.bucket_exists(bucket):
            self.client.make_bucket(bucket)
        self.client.put_object(
            bucket_name=bucket,
            object_name=object_name,
            data=file_data,
            length=-1,
            part_size=10*1024*1024
        )
        return f"http://{settings.MINIO_ENDPOINT}/{bucket}/{object_name}"

def get_minio_client():
    return MinioClient()