from fastapi import APIRouter, HTTPException
from app.models import Task
from app.database import db
from uuid import uuid4
from fastapi import Body

router = APIRouter()



@router.post("/tareas/")
def crear_tarea(tarea: Task):
    tarea_id = str(uuid4())
    db.collection("tareas").document(tarea_id).set(tarea.dict())
    return {"id": tarea_id, "mensaje": "Tarea creada correctamente"}

@router.get("/tareas/")
def listar_tareas():
    tareas = db.collection("tareas").stream()
    return [{tarea.id: tarea.to_dict()} for tarea in tareas]

@router.get("/tareas/{tarea_id}")
def obtener_tarea(tarea_id: str):
    doc = db.collection("tareas").document(tarea_id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.put("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: str, tarea: Task):
    db.collection("tareas").document(tarea_id).set(tarea.dict())
    return {"mensaje": "Tarea actualizada correctamente"}

@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: str):
    db.collection("tareas").document(tarea_id).delete()
    return {"mensaje": "Tarea eliminada correctamente"}

@router.patch("/tareas/{tarea_id}/completado")
def marcar_como_completado(tarea_id: str, completado: bool = Body(...)):
    doc_ref = db.collection("tareas").document(tarea_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    doc_ref.update({"completado": completado})
    return {"mensaje": f"Tarea actualizada: completado = {completado}"}