from fastapi import FastAPI
from app.backend.db import engine, Base
from app.models.task import Task
from app.models.user import User
from app.models import user

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user.router)

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}