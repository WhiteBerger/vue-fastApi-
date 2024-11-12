from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models import Movie as ModelsMovie
from typing import Any

class CRUDMovie(CRUDBase):

     def get_movie_by_year(self, db:Session,movie_year :Any):
          return db.query(self.model).filter(self.model.year==movie_year).all()
     
     def get_movie_by_name(self, db:Session,movie_name : Any):
          return db.query(self.model).filter(self.model.name.like('%'+movie_name + '%')).all()
     

crud_movie = CRUDMovie(ModelsMovie)
