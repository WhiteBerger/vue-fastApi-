from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api import deps
from crud import crud_anime
from schemas import anime as schemas_anime

router = APIRouter()

@router.get("/animes",response_model=list[schemas_anime.Anime])
def get_all_animes(
    db:Session = Depends(deps.get_db)
):
    animes = crud_anime.get_all(db=db)
    return animes

@router.get("/anime/{anime_name}",response_model=list[schemas_anime.Anime])
def get_anime_by_id(
     anime_name : str,
     db :Session = Depends(deps.get_db)
):
    anime = crud_anime.get_by_name(db=db,name=anime_name)
    return anime