from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String)

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    description: str

    class Config:
        from_attributes = True