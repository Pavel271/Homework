from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user_page(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_info(username: str = Query(...), age: int = Query(...)) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'