from typing import Optional
from pydantic import BaseModel


class Pronostico(BaseModel):
    id: Optional[str]
    lugar: str
    fecha: str
    max: str
    min: str
    descripcion: str
