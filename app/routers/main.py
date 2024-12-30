from fastapi import FastAPI
from app.backend.db import engine, Base
from app.models.task import Task
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}