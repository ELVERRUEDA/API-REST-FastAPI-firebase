from pydantic import BaseModel
from typing import Optional

class Tarea(BaseModel):
    titulo: str
    descripcion: Optional[str] = ""
    hora: Optional[str] = ""

class EstadoCompletado(BaseModel):
    completado: bool