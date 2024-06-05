from typing import Annotated
from pydantic import Field
from contrib.schemas import BaseSchema


class Categorias(BaseSchema):
    nome: Annotated[str, Field(description="Nome da Categoria", examples=["Scale"], max_length=10)]
