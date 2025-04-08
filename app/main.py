from fastapi import FastAPI
from app import routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas con FastAPI y Firebase"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)