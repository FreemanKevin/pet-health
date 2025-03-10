import pytest
from app.db.session import SessionLocal
from app.storage.minio_client import MinioClient

def test_postgres_connection():
    """测试 PostgreSQL 连接"""
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
        assert True, "✅ PostgreSQL 连接成功！"
    except Exception as e:
        pytest.fail(f"❌ PostgreSQL 连接失败: {e}")
    finally:
        db.close()

def test_minio_connection():
    """测试 MinIO 连接"""
    minio_client = MinioClient()
    try:
        buckets = minio_client.client.list_buckets()
        assert isinstance(buckets, list), "✅ MinIO 连接成功！"
    except Exception as e:
        pytest.fail(f"❌ MinIO 连接失败: {e}")