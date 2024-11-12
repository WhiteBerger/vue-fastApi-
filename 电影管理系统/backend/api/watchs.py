from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from crud import crud_watch
from schemas import watch as schemas_watch

router = APIRouter()

@router.get("/watch",response_model=list[schemas_watch.userwatchda])
def get_watchList_by_user_id(
    db:Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    watch= crud_watch.get_all_by_user_id(db=db,user_id=current_user.id)
    return watch


@router.post("/userwatch",response_model=schemas_watch.userwatch)
def create_watcHistory(
    watch_params : schemas_watch.data,
    db :Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    watch =crud_watch.create(db=db,watch_params=watch_params,user_id=current_user.id)
    return watch

@router.delete("/userwatch",response_model=schemas_watch.userwatchda)
def delet_all_user_watch_by_userId(
    db :Session =Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    watch= crud_watch.delete_allwatch_by_user_id(db=db ,user_id=current_user.id)
    return watch

@router.delete("/userwatch/{watch_id}",response_model=schemas_watch.userwatchda)
def delete_watch_by_id(
    watch_id : int,
    db :Session = Depends(deps.get_db),
):
    watch = crud_watch.delete_watch_by_id(db=db,id=watch_id)
    return watch

@router.get("/watch/{movie_name}",response_model=list[schemas_watch.userwatchda])
def search_movie_name(
    movie_name :str,
    db :Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    watch = crud_watch.search(db=db,movie_name=movie_name,user_id=current_user.id)
    return watch