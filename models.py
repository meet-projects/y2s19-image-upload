from sqlalchemy import Column, Integer, String, Boolean, PickleType, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    filename = Column(String) #filename
    title = Column(String)

