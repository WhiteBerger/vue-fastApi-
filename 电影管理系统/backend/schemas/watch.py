from datetime import datetime
from pydantic import BaseModel

class data(BaseModel):
     movie_id :int
     movie_name : str
     movie_image : str
class userwatch(data):
      user_id : int
      watchTime : datetime
class userwatchda(userwatch):
      id :int

      class Config:
          from_attributes = True 