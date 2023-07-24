import fastapi

from api.entities import UserBase

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user")
def create_user(user: UserBase):
	return user

