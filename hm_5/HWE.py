'''
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Создайте маршрут для обновления информации о пользователе (метод PUT).
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Создайте маршрут для отображения списка пользователей (метод GET).

Реализуйте валидацию данных запроса и ответа.

'''

from fastapi import FastAPI, Request, HTTPException
from typing import Optional
from pydantic import BaseModel
import logging

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: Optional[str] = None


user_1 = User(id=1, 
              name='Boris', 
              email='SFox@mail.ru', 
              password='h@rbinger765123')
user_2 = User(id=2, 
              name='Anna', 
              email='rosERainheart@mail.com', 
              password='l@vEAll!world!')
user_3 = User(id=3, 
              name='Rita', 
              email='funny+kitty@mail.com', 
              password='!`=("_")=`!')
user_4 = User(id=4, 
              name='Arthur', 
              email='GeniuScientist@mail.com', 
              password='NekvjhuesguyvGKFTGvtDTYHGVJguw')

users = [user_1, user_2, user_3, user_4]


@app.get("/users/")
async def user_list():
    global users
    logger.info(f'Обработан запрос для users')
    return {"users": users}


@app.post("/users/")
async def post_user(user: User):
    users.append(user)
    logger.info('Отработал POST запрос для создания задачи.')
    return user


@app.put("/users/{user_id}")
async def add_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
    logger.info(f'Отработал PUT запрос для user id = {user}.')
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return {"item_id": users.pop(i)}
    return HTTPException(status_code=404, detail='User not found')