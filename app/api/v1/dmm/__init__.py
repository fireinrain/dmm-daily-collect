from fastapi import APIRouter

from .dmm import router

dmm_router = APIRouter()
dmm_router.include_router(router, tags=["DmmDaily模块"])

__all__ = ["dmm_router"]
