from fastapi import APIRouter, HTTPException
from app.models import Task
from app.database import db

router = APIRouter()

# Crear tarea
@router.post("/tasks/")
def create_task(task: Task):
    doc_ref = db.collection("tasks").add(task.dict())
    return {"message": "Tarea creada correctamente"}

# Obtener tareas
@router.get("/tasks/")
def get_tasks():
    tasks = [{doc.id: doc.to_dict()} for doc in db.collection("tasks").stream()]
    return {"tasks": tasks}

# Actualizar tarea
@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):
    task_ref = db.collection("tasks").document(task_id)
    if not task_ref.get().exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task_ref.update(task.dict())
    return {"message": "Tarea actualizada"}

# Eliminar tarea
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    task_ref = db.collection("tasks").document(task_id)
    if not task_ref.get().exists:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task_ref.delete()
    return {"message": "Tarea eliminada"}
