from fastapi import APIRouter
from api.users import router as users_router
from api.auth import router as auth_router
from api.movies import router as movie_router
from api.watchs import router as watch_router
from api.animes import router as anime_router
api_router = APIRouter()
api_router.include_router(users_router, tags=["users"])
api_router.include_router(auth_router,tags=["auth"])
api_router.include_router(movie_router, tags=["电影"])
api_router.include_router(watch_router, tags=["观影记录"])
api_router.include_router(anime_router, tags=["动漫"])
@api_router.get("/")
def hello_world():
    return {"message": "Hello world"}
