from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel, Field

from pygments.lexer import default

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# path 传参
@app.get("/p/{article_id}")
# async def get_article_id(article_id: Annotated[int, Path(ge=2)]):
async def get_article(article_id: int=Path(ge=2)):
    return {"article_id": article_id}


# 查询传参
@app.get("/article/list")
# async def get_article_list(page: int = 1, page_size: int = 10):
#     return {"page": page, "page_size": page_size}

async def get_article_list(
        page: Annotated[int, Query(ge = 1)] = 1,
        size: Annotated[int, Query(ge = 10)] = 10
):
    return {"page": page, "size": size}


#body 传参

class LoginIn(BaseModel):
    # Field 的第一个参数：..., 代表该参数不能被省略，不能为空
    email: Annotated[str, Field(..., description="邮箱")]
    password: Annotated[str, Field(...,description="密码", min_length=6, max_length=20)]


# formdata = {
#     "email": "PlumYu1124@qq.com",
#     "password": "zhaoyun666"
# }
# data = LoginIn(**formdata)
# data = LoginIn(email=formdata['email'], password=formdata['password'])
@app.post("/login")
async def login(data: LoginIn):
    email = data.email
    password = data.password
    return {"email": email, "password": password}


# 依赖注入
from fastapi import Depends
from typing import Dict

async def page_common(page:int = 0, size: int = 10):
    return {"page": page, "size": size}

@app.get("/user/list")
async def get_user_list(page_params:Dict=Depends(page_common)):
    page = page_params["page"]
    size = page_params["size"]
    return {"page": page, "size": size}

@app.get("/movie/list")
async def get_movie_list(page_params:Dict=Depends(page_common)):
    page = page_params["page"]
    size = page_params["size"]
    return {"page": page, "size": size}