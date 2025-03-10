from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models.base import Base

class Medical(Base):
    __tablename__ = "medical_records"
    
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    visit_date = Column(Date, nullable=False)
    description = Column(String(255))
    
    pet = relationship("Pet", back_populates="medical_records")