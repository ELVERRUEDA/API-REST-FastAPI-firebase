# API REST con FastAPI y Firebase

## DESCRIPCION
Esta es una API REST construida con FastAPI y Firebase. Permite realizar autenticación de usuarios, manejar bases de datos en Firestore y ofrecer endpoints eficientes para el manejo de información.

## 🛠 Tecnologías
- FastAPI ⚡
- Firebase 🔥 (Firestore y Authentication)
- Uvicorn 🚀
- Python 🐍

## ## Instalación

1- Clona el repositorio:

```sh
git clone https://github.com/TU-USUARIO/API-REST-FastAPI-Firebase.git
cd API-REST-FastAPI-Firebase

2 - crea un entorno virtual

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows

3- instala dependencias 

pip install -r requirements.txt

4- configura firebase 

5- ejecuta el proyecto

Ejecuta el servidor con:
```sh
uvicorn app.main:app --reload

6 - uso de la api 

Endpoints principales 

- **GET /users** → Obtiene la lista de usuarios  
- **POST /users** → Crea un usuario  
- **GET /users/{id}** → Obtiene un usuario por ID  
- **DELETE /users/{id}** → Elimina un usuario  

7 licencia 

Este proyecto está bajo la Licencia MIT - Ver el archivo [LICENSE](LICENSE) para más detalles.
