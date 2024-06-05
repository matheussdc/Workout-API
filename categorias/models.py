from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from atleta.models import AtletaModel
from contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
