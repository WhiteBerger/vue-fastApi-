from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, Text, ForeignKey,VARCHAR
from sqlalchemy.orm import relationship

from db.config import Base


class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR) 
    year = Column(VARCHAR)
    image = Column(VARCHAR)
    video =Column(VARCHAR)