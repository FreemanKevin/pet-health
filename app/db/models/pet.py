from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.models.base import Base

class Pet(Base):
    __tablename__ = "pets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    species = Column(String(30))  # 猫/狗/其他
    breed = Column(String(50))    # 品种
    birth_date = Column(Date)
    owner_name = Column(String(100))
    chip_number = Column(String(50), unique=True)  # 芯片编号

    medical_records = relationship("Medical", back_populates="pet")
    vaccines = relationship("Vaccine", back_populates="pet")