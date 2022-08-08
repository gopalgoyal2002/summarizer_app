from fastapi import APIRouter
from apis import apis

router = APIRouter()

router.include_router(apis.router, tags=["summarize"])