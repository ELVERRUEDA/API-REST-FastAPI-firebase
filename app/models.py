from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False
