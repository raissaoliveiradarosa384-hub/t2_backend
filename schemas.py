from pydantic import BaseModel
from typing import Optional

class RoupaRegister(BaseModel):
    nome: str
    tamanho: str
    marca: str
    novo: bool
    preco: float

class RoupaResponse(BaseModel):
    nome: str
    tamanho: str
    marca: str
    id: int
    preco: float

class RoupaUpdate(BaseModel):
    nome: Optional[str] = None
    tamanho: Optional[str] = None
    marca: Optional[str] = None
    novo: Optional[bool] = None
    preco: Optional[float] = None

class Config:
    from_attributes: True #Ler ORM

