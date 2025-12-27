from fastapi import FastAPI

app = FastAPI()

# 定义 api
# get post put delete

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}