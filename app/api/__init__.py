from fastapi import APIRouter

from app.api import reported_phones, users, utils

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(reported_phones.router, tags=["reported_phones"])
