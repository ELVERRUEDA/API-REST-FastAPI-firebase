import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales de Firebase
cred = credentials.Certificate("D:\projects\fastAPI\venv\firebase-credentials.json")
firebase_admin.initialize_app(cred)

# Obtener referencia a la base de datos
db = firestore.client()

def get_db():
    return db
