from fastapi import APIRouter, HTTPException
from app.models import Tarea
from app.database import db
from uuid import uuid4
from fastapi import Body
from app.models import EstadoCompletado

router = APIRouter()

# Obtener todas las tareas
@router.get("/tareas/")
def obtener_tareas():
    tareas_ref = db.collection("tareas").stream()
    tareas = [{tarea.id: tarea.to_dict()} for tarea in tareas_ref]
    return tareas

# Crear una nueva tarea
@router.post("/tareas/")
def crear_tarea(tarea: Tarea):
    nueva_tarea_ref = db.collection("tareas").document()
    nueva_tarea_ref.set(tarea.dict())
    return {"id": nueva_tarea_ref.id, **tarea.dict()}

# Eliminar una tarea por ID
@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: str):
    tarea_ref = db.collection("tareas").document(tarea_id)
    if not tarea_ref.get().exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_ref.delete()
    return {"mensaje": "Tarea eliminada correctamente"}

# Editar una tarea por ID
@router.put("/tareas/{tarea_id}")
def editar_tarea(tarea_id: str, tarea: Tarea):
    tarea_ref = db.collection("tareas").document(tarea_id)
    if not tarea_ref.get().exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_ref.update(tarea.dict())
    return {"mensaje": "Tarea actualizada correctamente"}

# Marcar tarea como completada/incompleta
@router.patch("/tareas/{tarea_id}/completado")
def actualizar_estado_completado(tarea_id: str, estado: EstadoCompletado):
    tarea_ref = db.collection("tareas").document(tarea_id)
    if not tarea_ref.get().exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_ref.update({"completado": estado.completado})
    return {"mensaje": f"Tarea actualizada: completado = {estado.completado}"}