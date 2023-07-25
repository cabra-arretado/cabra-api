import fastapi

from api.entities.entities import User
from api.database.database import insert_user

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user")
def create_user(user: User):
	user_id = insert_user(user.email, user.password)
	return {"user_id": user_id}

