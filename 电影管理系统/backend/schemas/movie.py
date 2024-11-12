from datetime import datetime
from pydantic import BaseModel

class MovieBase(BaseModel):
     name : str
     year : str
class MovieBg(MovieBase):
      image : str
class Movie(MovieBg):
      id :int

      class Config:
          from_attributes = True 