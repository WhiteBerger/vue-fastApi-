from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from crud import crud_user
from schemas import user as schemas_user

router = APIRouter()

@router.post("/users", response_model=schemas_user.UserInDB)
def create_user(
    user_params: schemas_user.UserCreate,
    db: Session = Depends(deps.get_db)
):
    user = crud_user.get_by_email(db=db, email=user_params.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system."
        )
    user = crud_user.create(db=db, user_params=user_params)
    return user

@router.put("/users/name", response_model=schemas_user.UserInDB)
def update_user(
    user_params: schemas_user.UserUpdateName,
    db: Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    user = crud_user.update_name(db=db, id=current_user.id, user_params=user_params)
    return user

@router.put("/users/password", response_model=schemas_user.UserInDB)
def update_user(
    user_params: schemas_user.UserUpdatePassword,
    db: Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    user = crud_user.update_password(db=db, id=current_user.id, user_params=user_params)
    return user
@router.get("/users/{user_email}",response_model=schemas_user.UserInDB)
def get_user_by_userEmail(
    user_email:str,
    db:Session = Depends(deps.get_db)
):
    user = crud_user.get_by_email(db=db,email=user_email)
    return user

@router.post("/users/{user_email}",response_model=schemas_user.UserInDB)
def get_user_by_userEmail(
    user_email:str,
    db:Session = Depends(deps.get_db)
):
    user = crud_user.get_by_email(db=db,email=user_email)
    return user

@router.delete("/user",response_model=schemas_user.UserInDB)
def delete_user_by_id(
    db :Session =Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    user = crud_user.remove(db=db,name=current_user.id)
    return user

