from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models import Anime as ModelsAnime
from typing import Any

class CRUDAnime(CRUDBase):

     def get_anime_by_year(self, db:Session,anime_year :Any):
          return db.query(self.model).filter(self.model.year==anime_year).all()
     
     def get_anime_by_name(self, db:Session,anime_name : Any):
          return db.query(self.model).filter(self.model.name.like('%'+anime_name + '%')).all()
     

crud_anime = CRUDAnime(ModelsAnime)