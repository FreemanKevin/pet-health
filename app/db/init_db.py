from app.db.session import engine
from app.db.models.base import Base
from app.db.models import pet, medical, vaccine

def init_db():
    Base.metadata.create_all(bind=engine)