from datetime import datetime
from pydantic import BaseModel

class AnimeBase(BaseModel):
     name : str
     year : str
class AnimeBg(AnimeBase):
      image : str
      id :int
class Anime(AnimeBg):
      video : str

      class Config:
          from_attributes = True 