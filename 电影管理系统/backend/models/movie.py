from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, Text, ForeignKey,VARCHAR
from sqlalchemy.orm import relationship

from db.config import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR,nullable=False) 
    year = Column(VARCHAR, nullable=False)
    image = Column(VARCHAR,nullable=False)
    watch = relationship("Watch",uselist=True,back_populates="movie")