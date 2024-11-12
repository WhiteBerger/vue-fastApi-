from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, Text, ForeignKey,VARCHAR
from sqlalchemy.orm import relationship
from db.config import Base

class Watch(Base):
    __tablename__ = "watch"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=True)
    movie_name = Column(VARCHAR,nullable=False)
    movie_image = Column(VARCHAR,nullable=False)
    watchTime = Column(TIMESTAMP(timezone=True),default=datetime.utcnow, nullable=True)
    user = relationship("User", back_populates="watch")
    movie = relationship("Movie", back_populates="watch")