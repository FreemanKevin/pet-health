# pet-health

## 项目结构

```shell
/pet-health
├── app/                          # 主应用目录
│   ├── api/                      # API路由层
│   │   ├── v1/                  # API版本管理
│   │   │   ├── __init__.py
│   │   │   ├── pets.py          # 宠物相关路由
│   │   │   ├── medical.py       # 医疗记录路由
│   │   │   └── vaccines.py      # 疫苗记录路由
│   ├── core/                    # 核心配置
│   │   ├── config.py           # 环境配置
│   │   └── security.py         # 安全相关（预留）
│   ├── db/                      # 数据库模块
│   │   ├── models/             # 数据模型
│   │   │   ├── pet.py
│   │   │   ├── medical.py
│   │   │   └── base.py        # 基础模型
│   │   ├── repositories/       # 数据库操作层
│   │   ├── session.py          # 数据库会话管理
│   │   └── init_db.py          # 数据库初始化
│   ├── dependencies/           # 依赖项
│   │   └── database.py         # 数据库依赖注入
│   ├── storage/                # 文件存储模块
│   │   ├── minio_client.py     # MinIO客户端
│   │   └── schemas.py         # 文件上传响应模型
│   ├── schemas/                # Pydantic模型
│   │   ├── pet.py
│   │   ├── medical.py
│   │   └── vaccine.py
│   ├── utils/                  # 工具类
│   ├── main.py                 # 应用入口
│   └── health.py              # 健康检查端点
├── tests/                      # 测试目录
│   ├── __init__.py
│   ├── conftest.py            # 测试配置
│   ├── test_pets.py
│   └── test_medical.py
├── docker-compose.yml          # 容器编排
├── Dockerfile                  # 后端镜像构建
├── requirements.txt           # 依赖列表
├── .env                        # 环境变量配置
└── README.md
```

## 环境配置

请确保在项目根目录下创建一个 `.env` 文件，并添加以下内容：

```plaintext
# PostgreSQL 配置
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=pet_health_db
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# MinIO 配置
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_SECURE=False
MINIO_BUCKET=pet-health
```

## 运行应用

1. 安装依赖：

```shell
pip install -r requirements.txt
```

2. 启动应用：

```shell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

3. 使用 Docker Compose 启动应用：

```shell
docker-compose up --build
```


