from typing import Optional
import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
      
      TITLE : Optional[str] ="电影列表接口"

      DESC : Optional[str] = """
      -电影列表项目，基于Hello Flask 一书中的实战项目
      -实现：FASTAPI
      """

      #JWT

      SECRET_KEY :str = secrets.token_urlsafe(32)
      ALGORITHM : str = "HS256" #加密算法
      ACCESS_TOKEN_EXPIRE_MINUTES : int = 60 * 24 * 7


settings =Settings()