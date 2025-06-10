from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    friends: list[int] = []

external_data = {
    "id": 1,
    "name": "John",
    "email": "john@example.com",
    "password": "password123",
    "friends": [2, 3]
}

user = User(**external_data)
print(user)

print(user.id)