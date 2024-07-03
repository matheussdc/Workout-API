from fastapi import APIRouter
from atleta.controller import router as atleta
from categorias.controller import router as categorias

api_router = APIRouter()

api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])

api_router.include_router(atleta, prefix='/atleta', tags=['atletas'])
