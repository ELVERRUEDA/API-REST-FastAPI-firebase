from fastapi import FastAPI
from app import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas con FastAPI y Firebase"}
