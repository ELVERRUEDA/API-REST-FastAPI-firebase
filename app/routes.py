from fastapi import APIRouter, Depends
from models import User
from database import get_db

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: str, db=Depends(get_db)):
    user = db.collection("users").document(user_id).get()
    if user.exists:
        return user.to_dict()
    return {"error": "User not found"}
