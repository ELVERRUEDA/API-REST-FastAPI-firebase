from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Crear instancia de FastAPI
app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    nombre: str
    descripcion: str
    precio: float

# Ruta de prueba
@app.get("/")
def home():
    return {"mensaje": "API con FastAPI y Firebase"}

# Ruta para agregar un item a Firestore
@app.post("/items/")
def create_item(item: Item):
    doc_ref = db.collection("items").add(item.dict())
    return {"mensaje": "Item agregado correctamente"}

# Ruta para obtener todos los items
@app.get("/items/")
def get_items():
    docs = db.collection("items").stream()
    items = [{doc.id: doc.to_dict()} for doc in docs]
    return {"items": items}
