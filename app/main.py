from fastapi import FastAPI
from backend.db import engine, Base
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(user_router)
app.include_router(task_router)