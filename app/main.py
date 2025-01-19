from fastapi import FastAPI
from app.models.users import User
from app.models.roles import Role

app = FastAPI()

users = [
    User(id=1, last_name="Doe", first_name="John", email="john.doe@example.com", phone="1234567890"),
    User(id=2, last_name="Smith", first_name="Jane", email="jane.smith@example.com", phone="0987654321"),
]

roles = [
    Role(id=1, name="Admin", user=users[0], description="Administrator role"),
    Role(id=2, name="User", user=users[1], description="Regular user role"),
]

@app.get("/users/")
def get_users():
    return users

@app.get("/roles/")
def get_roles():
    return roles
