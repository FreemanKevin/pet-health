from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models.base import Base

class Vaccine(Base):
    __tablename__ = "vaccines"
    
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    vaccine_date = Column(Date, nullable=False)
    vaccine_name = Column(String(255))
    
    pet = relationship("Pet", back_populates="vaccines")
