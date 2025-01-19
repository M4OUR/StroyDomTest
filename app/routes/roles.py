from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_roles():
    return [{"id": 1, "name": "Admin", "description": "Administrator role"}]
