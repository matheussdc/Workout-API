from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, status, Body, HTTPException
from sqlalchemy import select

from atleta.models import AtletaModel
from atleta.schemas import AtletaIn, AtletaOut
from categorias.models import CategoriaModel
from centro_treinamento.models import CentroTreinamentoModel
from contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post('/',
             summary="Criar novo atleta",
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut,
             )
async def post(
        db_session: DatabaseDependency,
        atleta_in: AtletaIn = Body(...)
) -> AtletaOut:
    categoria_nome = atleta_in.categoria.nome
    centro_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Categoria {categoria_nome} não foi encontrada'
        )

    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_nome))).scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Centro de Treinamento {centro_nome} n]ao foi encontrado'
        )
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Erro ao inserir dados'
        )

    return atleta_out
