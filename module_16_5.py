from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from contextlib import asynccontextmanager
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@asynccontextmanager
async def lifespan(app: FastAPI):
    users.append(User(id=1, username='UrbanUser ', age=24))
    users.append(User(id=2, username='UrbanTest', age=22))
    users.append(User(id=3, username='Capybara', age=60))
    yield

@app.get('/', response_class=HTMLResponse)
async def all_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/users/{user_id}', response_class=HTMLResponse)
async def one_user(request: Request, user_id: int) -> HTMLResponse:
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})

@app.post('/user/{username}/{age}', response_model=User)
def create_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{user_name}/{age}', response_model=str)
async def update_user(user_name: Annotated[str, Path(min_length=5, max_length=20)],
        age: int = Path(ge=18, le=120, description='Введите возраст', examples=55),
        user_id: int = Path(ge=0)) -> str:
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = user_name
            existing_user.age = age
            return f'Пользователь {user_id} обновлён'
    raise HTTPException(status_code=404, detail='Пользователь не найден.')

@app.delete('/user/{user_id}', response_model=User)
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail='Пользователь не найден')