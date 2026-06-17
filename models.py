from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import Base


class Roupa(Base):
    __tablename__ = "Roupas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    tamanho: Mapped[str] = mapped_column(String, nullable=False)

    marca: Mapped[str] = mapped_column(String, nullable=False)

    novo: Mapped[bool] = mapped_column(Boolean, nullable=False)

    preco: Mapped[float] = mapped_column(Integer, nullable=False)


