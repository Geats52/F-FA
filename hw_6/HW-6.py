'''
Напишите API для управления списком задач. Для этого создайте модель Task
со следующими полями:
○ id: int (первичный ключ)
○ title: str (название задачи)
○ description: str (описание задачи)
○ done: bool (статус выполнения задачи)

API должно поддерживать следующие операции:
○ Получение списка всех задач: GET /tasks/
○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
○ Создание новой задачи: POST /tasks/
○ Обновление информации о задаче: PUT /tasks/{task_id}/
○ Удаление задачи: DELETE /tasks/{task_id}/
Для валидации данных используйте параметры Field модели Task.
Для работы с базой данных используйте SQLAlchemy и модуль databases.

'''

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

DATABASE_URL = "sqlite:///mydatabase_6.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table("tasks", 
                         metadata, 
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
                         sqlalchemy.Column("title", sqlalchemy.String(25)), 
                         sqlalchemy.Column("description", sqlalchemy.String(250)),
                         sqlalchemy.Column("done", sqlalchemy.Boolean(False)),
                         )
engine = sqlalchemy.create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
    )
metadata.create_all(engine)

app = FastAPI()

class TaskIn(BaseModel):    
    title: str = Field(max_length=25)
    description: str = Field(min_length=25)
    done: bool = Field(default=False)

class Task(BaseModel):    
    id: int
    title: str = Field(max_length=25)
    description: str = Field(min_length=25)
    done: bool = Field(default=False)



@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)

@app.post("/tasks/", response_model=Task)
async def write_task(task: TaskIn):
    query = tasks.insert().values(**task.dict())
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": task_id}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}
