from fastapi import FastAPI, HTTPException, Path
from typing import Dict, Annotated

app = FastAPI()
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
def get_users():
    return users

@app.post('/user/{username}/{age}')
def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя пользователя")],
        age: Annotated[int, Path(ge=18, le=120, description="Введите возраст")]):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} зарегистрирован'

@app.put('/user/{user_id}/{username}/{age}')
def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Введите ID пользователя")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя пользователя")],
        age: Annotated[int, Path(ge=18, le=120, description="Введите возраст")]):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    users[user_id_str] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id_str} был обновлён'

@app.delete('/user/{user_id}')
def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Введите ID пользователя")]):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    del users[user_id_str]
    return f'Пользователь {user_id_str} был удалён'