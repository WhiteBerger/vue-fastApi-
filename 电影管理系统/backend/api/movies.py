from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from crud import crud_movie
from schemas import movie as schemas_Movie

router = APIRouter()

@router.get("/movies",response_model=list[schemas_Movie.Movie])
def get_all_movies(
    db:Session =Depends(deps.get_db)
):
    movies = crud_movie.get_all(db=db)

    return movies

@router.get("/movieT/{movie_year}",response_model = list[schemas_Movie.Movie])
def get_movie_by_year(
    movie_year : str,
    db :Session =Depends(deps.get_db)
):
    movies = crud_movie.get_movie_by_year(db=db,movie_year=movie_year)
    return movies

@router.get("/movieN/{movie_name}",response_model = list[schemas_Movie.Movie])
def get_movie_by_name(
    movie_name : str,
    db :Session =Depends(deps.get_db)
):
    movies = crud_movie.get_movie_by_name(db=db,movie_name=movie_name)
    return movies
