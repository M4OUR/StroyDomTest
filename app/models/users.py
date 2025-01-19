from pydantic import BaseModel

class User(BaseModel):
    id: int
    last_name: str
    first_name: str
    email: str
    phone: str
