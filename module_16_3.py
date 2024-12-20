from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
def get_users():
    return users

@app.post('/user/{username}/{age}')
def create_user(username: str, age: int):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь  {user_id} зарегистрирован'

@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} был обновлён'

@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    del users[user_id]
    return f'Пользователь {user_id} был удалён'