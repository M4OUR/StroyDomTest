from pydantic import BaseModel
from app.models.users import User

class Role(BaseModel):
    id: int
    name: str
    user: User
    description: str
