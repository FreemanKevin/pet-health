from fastapi import FastAPI
from app.api.v1 import pets, medical, vaccines
from app.db.init_db import init_db
from app.core.config import settings
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    try:
        logger.info("正在初始化数据库...")
        init_db()
        logger.info("数据库初始化成功！")
    except Exception as e:
        logger.error(f"数据库初始化失败: {e}")
        raise  # 抛出异常，阻止应用启动

@app.get("/")
def read_root():
    return {"message": "Pet Health Management System"}

app.include_router(pets.router)
app.include_router(medical.router)
app.include_router(vaccines.router)