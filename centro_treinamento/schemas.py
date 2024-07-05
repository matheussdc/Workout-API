from typing import Annotated
from pydantic import PositiveFloat, Field, UUID4
from contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", examples=["CT Power"], max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de Treinamento", examples=["Rua A, 123"], max_length=60)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do Centro de Treinamento", example="Tom Cruise", max_length=30)]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", examples=["CT Power"], max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]