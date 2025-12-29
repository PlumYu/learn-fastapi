from random import seed

from fastapi import FastAPI,Depends
from sqlalchemy import select, delete, update

import models
from models import AsyncSession
from dependencies import get_session
from models.user import User
from schemas import UserSchema, UserListSchemaOut

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/user/add", response_model=UserSchema)
async def add_user(session: AsyncSession = Depends(get_session)):

    # 开启事物
    async with session.begin():
        user = User(
            email="PlumYu1@qq.com",
            username="PlumYu1124",
            password="123456",
            mobile="1845587654")
        session.add(user)
    return user

@app.get('/user/select/{user_id}', response_model=UserSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = select(User).where(User.id == user_id)
        # result = await session.execute(stmt)
        # user = result.scalars().first()
        user = await session.scalar(stmt)
        return user

@app.get('/user/select', response_model=UserListSchemaOut)
async def get_user(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = select(User).where(User.email.contains("qq"))
        # result = await session.execute(stmt)
        # user = result.scalars().first()
        users = await session.scalars(stmt)
        return {"users": users}

@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = delete(User).where(User.id == user_id)
        await session.execute(stmt)
        return {"message": "User deleted"}

@app.put('/user/update/{user_id}')
async def update_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        # 1.先查找再修改
        # user = await session.scalar(select(User).where(User.id == user_id))
        # user.username = "ZFei"
        # 2.直接修改
        user = await session.execute(update(User).where(User.id == user_id).values(username="ZYun"))
    return {"Message": "User updated"}
