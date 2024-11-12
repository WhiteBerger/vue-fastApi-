from typing import Generator
from db.config import SessionLocal
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt
from core import security,settings
from crud import crud_user
from schemas import token as schemas_token

def get_db() -> Generator:
    db = SessionLocal()
    try:
         yield db
    finally:
        db.close()

reusable_oauth2 = OAuth2PasswordBearer (tokenUrl="/api/login/access_token")

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
):
    try:
        #使用decode，通过security导入的SECRET_KEY密钥解密，变为明文。
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = schemas_token.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )

    user = crud_user.get_by_id(db, id=token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user